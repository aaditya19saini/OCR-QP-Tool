"""Local OCR of page images with PaddleOCR-VL 1.6 (llama.cpp server, runs on this machine's GPU).

Usage: python -m pyq.ocr [year ...]      (default: every year in papers.yaml)
Output: data/ocr/<year>/pNNN.md          (committed; resumable: existing pages are skipped)
Needs: ~/.cache/pyq-ocr/ with llama/llama-server, the PaddleOCR-VL GGUF, its mmproj and chat_template.jinja
       (override the folder with PYQ_OCR_HOME).
"""
import base64
import json
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

from .common import PAGES, ROOT, load_yaml, setup_logging, verify_manifest
from .render import render

OCR = ROOT / "data" / "ocr"
HOME = Path(os.environ.get("PYQ_OCR_HOME", Path.home() / ".cache" / "pyq-ocr"))
PORT = 8931
URL = f"http://127.0.0.1:{PORT}"


def start_server() -> subprocess.Popen:
    # CUDA build uses the NVIDIA GPU (~10 s/page); the Vulkan build only sees the iGPU here (~45 s/page).
    cuda = HOME / "llama-cuda" / "llama-server"
    binary = cuda if cuda.exists() else HOME / "llama" / "llama-server"
    env = {**os.environ, "LD_LIBRARY_PATH": f"/opt/cuda/lib64:{os.environ.get('LD_LIBRARY_PATH', '')}"}
    cmd = [
        str(binary),
        "-m", str(HOME / "PaddleOCR-VL-1.6-GGUF.gguf"),
        "--mmproj", str(HOME / "PaddleOCR-VL-1.6-GGUF-mmproj.gguf"),
        "--jinja", "--chat-template-file", str(HOME / "chat_template.jinja"),
        "-ngl", "99", "-c", "8192",  # default 131k context does not fit a 4 GB GPU
        "--port", str(PORT), "--temp", "0",
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, env=env)
    for _ in range(120):
        try:
            if json.load(urllib.request.urlopen(f"{URL}/health", timeout=2)).get("status") == "ok":
                return proc
        except OSError:
            pass
        if proc.poll() is not None:
            raise RuntimeError(f"llama-server exited with {proc.returncode}")
        time.sleep(1)
    proc.kill()
    raise RuntimeError("llama-server did not become healthy in 120 s")


def ocr_page(png: Path) -> str:
    img = base64.b64encode(png.read_bytes()).decode()
    body = json.dumps({
        "messages": [{"role": "user", "content": [
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img}"}},
            {"type": "text", "text": "OCR:"},
        ]}],
        # densest page so far ~2.5k chars (~1k tokens); the cap mostly bounds whitespace loops after the footer
        "temperature": 0, "max_tokens": 2048,
    }).encode()
    req = urllib.request.Request(f"{URL}/v1/chat/completions", body, {"Content-Type": "application/json"})
    r = json.load(urllib.request.urlopen(req, timeout=600))
    choice = r["choices"][0]
    return clean(choice["message"]["content"], choice.get("finish_reason"), png)


def clean(text: str, finish_reason: str | None, png: Path) -> str:
    """Hitting max_tokens is only OK when the model was looping on whitespace after the real text."""
    if finish_reason == "length" and len(text) - len(text.rstrip()) < 200:
        raise RuntimeError(f"{png}: OCR output truncated at max_tokens")
    return text.strip() + "\n"


def main(years: list[int]) -> None:
    years = years or sorted(load_yaml("papers.yaml")["papers"])
    for y in years:  # render first: render() starts its own log file
        if not (PAGES / str(y)).exists():
            render(y)
    log = setup_logging("ocr")
    verify_manifest()
    log.info("model dir %s", HOME)
    proc = start_server()
    try:
        for y in years:
            out = OCR / str(y)
            out.mkdir(parents=True, exist_ok=True)
            todo = [p for p in sorted((PAGES / str(y)).glob("p*.png")) if not (out / f"{p.stem}.md").exists()]
            log.info("%d: %d pages to OCR", y, len(todo))
            for png in todo:
                t = time.time()
                text = ocr_page(png)
                (out / f"{png.stem}.md").write_text(text)
                log.info("%d %s %.0fs %d chars", y, png.stem, time.time() - t, len(text))
    finally:
        proc.terminate()
        proc.wait(timeout=30)


if __name__ == "__main__":
    main([int(a) for a in sys.argv[1:]])

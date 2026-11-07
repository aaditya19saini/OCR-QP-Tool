# JAM MS: what to study from, in what order

Researched 2026-11-07 for **JAM 2027 (14 Feb 2027, afternoon session)**. The setup this guide assumes: about 14 weeks left, a weak base, and free resources plus cheap Indian-edition books.
Topic weights come from this repo's report (`outputs/report/jam_ms_report.pdf`, 12 papers, 2015–2026). Tags: **FACT** = checked against the source. **INFERENCE** = my reasoning from facts. **UNCERTAIN** = thin or conflicting evidence.

## TL;DR

1. **Past papers are the main resource.** Every topper interview I found says so. You already have 14 official papers in `data/raw/`, plus JAM 2026 (link below). Your report shows 43.6% of questions reuse an earlier problem structure.
2. **One book per subject, not five.** Stats: Hogg, McKean & Craig for theory, plus Gupta & Kapoor (FMS) for drill. Maths: NCERT/JEE-level calculus first, then Strang for matrices.
3. **Free video for a weak base:** NPTEL (Somesh Kumar, IIT KGP) for probability and inference, MIT 18.06 (Strang) for matrices, Harvard Stat 110 for probability intuition.
4. **The new 2026-syllabus topics were tested in JAM 2026: 9 questions, 14 of 100 marks** (FACT, classified and reviewed): Markov chains ×2, Poisson process, runs test, sign test, matrix definiteness, descriptive statistics ×3 (CV, mean/median/IQR, Spearman). Don't skip them. One paper only, so their future weight is unknown (UNCERTAIN).
5. **Mocks:** the official mock is free and uses the real interface. Use it in the final weeks. Your own timed past papers are the real mock series.

## 1. Time split (from the report)

Use 90% of your time in proportion to past marks (12 papers) and 10% on the new topics in section 4.

| Topic | Study time | Tier-1 subtopics to master (in ≥80% of papers or ≥2% of marks) |
|---|---|---|
| Univariate Distributions | 13.1% | CDF/PMF/PDF; standard discrete distributions; expectation, moments, quantiles; MGFs |
| Estimation | 12.5% | MLE; unbiasedness & consistency; UMVUE / Rao-Blackwell / Lehmann-Scheffé; confidence intervals |
| Multivariate Distributions | 9.9% | Joint/marginal/conditional; covariance & correlation |
| Matrices and Determinants | 8.8% | Eigenvalues & Cayley-Hamilton; systems of linear equations |
| Integral Calculus | 7.3% | Areas/volumes/arc length; FTC & Leibniz rule |
| Differential Calculus (1 var) | 6.9% | Differentiability; Rolle's / MVT |
| Testing of Hypotheses | 6.5% | Errors, size, power, p-value; Neyman-Pearson / MP tests |
| Probability | 6.3% | Conditional probability & Bayes |
| Sequences and Series | 5.6% | Convergence tests |
| Sampling Distributions | 5.1% | (χ², t, F, order statistics; no Tier-1 subtopic) |
| Limit Theorems | 4.4% | CLT; laws of large numbers |
| Differential Calculus (2 var) | 2.6% | (maxima/minima, partials) |
| **2026-syllabus new topics** | **10%** | see section 4 |

Skip differential equations. They haven't appeared since 2016 and aren't in the 2026 syllabus (FACT, report).

## 2. Resources by topic

Cheap = Indian edition, roughly ₹600–1,000 at time of search (retailer snapshots, prices move).

### Statistics (about 65% of marks, 2015–2026)

| Topic | Learn (free video) | Read (one book) | Practise |
|---|---|---|---|
| Probability | Harvard **Stat 110** (Blitzstein): YouTube lectures, free online book [1]. NPTEL **Probability and Statistics**, Somesh Kumar [2] | Gupta & Kapoor (FMS) ch. on probability. NCERT Class 12 first if the base is weak [3] | Stat 110 strategic practice problems with solutions; JAM PYQs |
| Univariate & Multivariate Distributions, MGFs | NPTEL Somesh Kumar [2]; MIT **18.05** [4] | **Hogg, McKean & Craig**, ch. 1–3 [5][6] | Hogg exercises; FMS examples (one topper says do the examples, skip the exercises [3]); MIT 18.05 problem sets with solutions [4] |
| Sampling Distributions, Limit Theorems | NPTEL [2]; MIT 18.05 [4] | Hogg (sampling distributions & limiting distributions chapters) | PYQs (CLT appears in 10 of 11 papers) |
| Estimation | NPTEL **Statistical Inference** (Somesh Kumar, IIT KGP, or Niladri Chatterjee, IIT Delhi) [7] | Hogg; **Rohatgi & Saleh** for depth [3][8]; Mood, Graybill & Boes is a topper favourite for inference [6] | PYQs; Rohatgi exercises |
| Testing of Hypotheses | NPTEL Statistical Inference [7] | Hogg (NP lemma, MP/UMP tests) | PYQs |

### Mathematics (about 35% of marks)

| Topic | Learn (free video) | Read | Practise |
|---|---|---|---|
| Matrices & Determinants | MIT **18.06**, Gilbert Strang: videos, problem sets and exams, all with solutions [9]. Hindi: Dr. Gajendra Purohit (YouTube/Unacademy) [3][10] | Strang's lectures are enough; one topper says no separate book is needed [3] | JAM MS + JAM MA + CSIR-NET linear algebra PYQs [3] |
| Sequences & Series | NPTEL **Real Analysis I** (IIT Palakkad) [11] | S.K. Mapa, *Introduction to Real Analysis*, ch. 5–6 [3], or Bartle & Sherbert / Shanti Narayan [6] | Schaum's; PYQs [6] |
| Differential Calculus (1 & 2 var) | JEE-level calculus videos (any) [3][6] | NCERT 11–12 → JEE material [6]; Berman, *Problem Book in Mathematical Analysis*, for limits [3] | JAM PYQs + JEE Main calculus questions [3] |
| Integral Calculus | same | Anton & Bivens, *Calculus* [6] | PYQs; drill Leibniz rule (Tier 1) |

**Weak-base order (INFERENCE):** NCERT 11–12 calculus and probability (1–2 weeks) → Stat 110 / NPTEL probability → Hogg → inference. Hogg and Rohatgi are hard first reads. Gupta & Kapoor is the gentler on-ramp.

## 3. Practice and mocks

| What | Where | Notes |
|---|---|---|
| Official PYQs 2012–2025 | `data/raw/` in this repo; also jam2026.iitb.ac.in → Previous Year Question Papers [12] | Answer keys are printed in 2016–2018 and 2024 |
| **JAM 2026 MS paper + key** | jam2026.iitb.ac.in/files/MS_QP.pdf and MS_AK.pdf [13] | The **only** paper set on the 2026 syllabus. Save it for a full timed mock |
| Official mock (real CBT interface) | JAM 2026 mock page lists an MS mock [14]. JAM 2027 mock (IIT KGP) not out yet [15] | Use it to practise the on-screen calculator and the MSQ/NAT entry. One topper flagged this [6] |
| Neighbouring PYQs for extra drill | JAM MA (maths), ISI M.Stat, GATE ST [6][16] | AIR 2 and AIR 32 (2021) both used these |
| Free PYQ walk-throughs | Unacademy free JAM MS 2026 discussion [17]; Cheenta written/video solutions (2021) [18] | Coverage is patchy; I found no free channel solving every year |
| Free online mock tests | Unacademy "All India Mock Test" for MS (free listings for 2025 and 2026) [19] | Quality unverified. The official mock + timed PYQs is the safer core |

**How to use PYQs** (from the toppers [6][16][20]): solve by topic while learning, keep the last 3–4 years for timed full mocks, and keep an error notebook you reread before each mock. Attempt in the order MCQ → NAT → MSQ, and drop a question after about 5 minutes. MSQs have no partial credit, so attempt only the ones you're sure of.

## 4. The 2026-syllabus topics (new in JAM 2026)

**FACT (JAM 2026 paper: every page image-checked; questions classified and independently reviewed):** 9 questions covered subtopics that never appeared in 2015–2025:

| Q | Marks | Topic |
|---|---|---|
| 3 | 1 | Definiteness of a symmetric matrix (quadratic forms) |
| 9 | 1 | Markov chain, stationary distribution |
| 28 | 2 | Runs test |
| 17 | 2 | Descriptive statistics (coefficient of variation vs SD) |
| 29 | 2 | Markov chain, irreducibility |
| 33 | 2 | Descriptive statistics (sample mean vs median, MSQ) |
| 43 | 1 | Spearman's rank correlation (correction) |
| 49 | 1 | Poisson process |
| 59 | 2 | Sign test |

That's 14/100 marks. Still untested anywhere: Kolmogorov–Smirnov / empirical CDF, Mann–Whitney, skewness/kurtosis, two-variable limits. One paper doesn't make a trend (UNCERTAIN), but it rules out skipping these topics.

| Topic | Free | Book |
|---|---|---|
| Markov chains, Poisson process | MIT **6.041** (Tsitsiklis): Poisson lectures 14–15, Markov chains 16–18 (2010 numbering), problem sets and exams with solutions [21]. **probabilitycourse.com** (Pishro-Nik), free full textbook [22]. **Grinstead & Snell**, free (GNU FDL), ch. 11 Markov chains [23]. NPTEL, Dharmaraja (IIT Delhi) [24] | Stat 110 book also has a Markov chains chapter [1] |
| Sign, runs, Mann-Whitney, K-S / empirical CDF | NPTEL **Non-Parametric Statistical Inference**, Niladri Chatterjee (IIT Delhi), 4 weeks; noc25_ma63 covers sign, runs and Mann-Whitney [25] | Rohatgi & Saleh, ch. 13 "Nonparametric Statistical Inference" [8]; Gibbons & Chakraborti (the NPTEL reference) [25] |
| Descriptive statistics (moments, skewness, kurtosis, correlation) | — | Gupta & Kapoor covers these at the level JAM tests (INFERENCE) |
| Quadratic forms, definiteness | MIT 18.06, positive-definite lectures [9] | Strang |
| Limits/continuity in 2 variables | NPTEL Basic Real Analysis covers several variables [11] | any calculus text |

## 5. A 14-week plan (INFERENCE; adjust to taste)

| Weeks | Do |
|---|---|
| 1–2 | NCERT/JEE calculus + probability refresher. Start Stat 110 lectures 1–10. Solve the probability and calculus PYQs from 2015–2018 |
| 3–6 | Distributions (uni + multi), MGFs, sampling distributions, CLT: NPTEL + Hogg + FMS. In parallel: Strang for matrices |
| 7–9 | Estimation and testing: NPTEL inference + Hogg/Rohatgi. Maths: sequences & series, integral calculus |
| 10 | New topics (section 4): 6.041 Markov/Poisson lectures, NPTEL nonparametric (4 weeks of content, skim the relevant weeks) |
| 11–12 | Timed full papers 2019–2023 (3 h each), error notebook, patch weak topics |
| 13 | Official mock interface + JAM 2024, 2025 timed |
| 14 | JAM 2026 paper as the final mock; revise the formula sheet and error notebook; lighter days before 14 Feb |

## 6. Where the sources disagree

- **Gupta & Kapoor:** one topper (AIR 32) dropped it [6]. Another prep blog calls it the primary resource and practised it 8–10 times [3]. My read (INFERENCE): it's good for drill and coverage, weaker for inference theory. Use Hogg for that.
- **Mocks vs concepts:** AIR 4 (2021) says concept building matters more than mock tests [20]. AIR 2 and AIR 32 lean heavily on timed PYQ mocks [6][16]. With a weak base, concepts come first. Switch to timed papers by week 11.
- **Books toppers name are mostly 2021 interviews**, before the 2026 syllabus change. None of them covered nonparametrics or Markov chains.

## 7. Limitations

- Topper evidence is self-reported, mostly from Cheenta (a coaching site), and mostly 2021. A 2026 topper credits the PW test series, which is paid [26].
- I didn't watch the courses or rate their quality. The picks rest on syllabus match and repeated recommendations.
- The JAM 2027 syllabus isn't on the IIT KGP site yet [15]. I assumed it matches 2026 (UNCERTAIN).
- Prices are retailer snapshots from search results [27].
- The JAM 2026 counts rest on one paper. Topic labels are model judgements, reviewed by a second model pass (all 9 new-topic filings confirmed).
- I didn't check whether NPTEL runs these courses live in Jan–Apr 2027. The archived videos are free either way.

## Sources

1. Harvard Stat 110 (course site; free book via probabilitybook.net, YouTube lectures): https://stat110.hsites.harvard.edu/
2. NPTEL Probability and Statistics, Somesh Kumar (IIT KGP): https://nptel.ac.in/courses/111105090 · https://onlinecourses.nptel.ac.in/noc25_ma49/preview
3. "Cracking IIT JAM Mathematical Statistics" (prep blog): https://shailza2106.github.io/Statistics/iitjam_art1.html
4. MIT 18.05 (Spring 2022) problem sets with solutions: https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/pages/problem-sets
5. Careers360, how to prepare for JAM MS: https://university.careers360.com/articles/how-prepare-jam-mathematical-statistics
6. Abhinav Shukla, AIR 32, JAM MS 2021 (Cheenta): https://cheenta.com/?p=88514
7. NPTEL Statistical Inference: https://onlinecourses.nptel.ac.in/noc22_ma33/preview (IIT KGP) · https://onlinecourses.nptel.ac.in/noc20_ma19/preview
8. Rohatgi & Saleh, 3rd ed. contents (ch. 13 nonparametrics): https://www.oreilly.com/library/view/an-introduction-to/9781118799642/c13.xhtml
9. MIT 18.06 Linear Algebra (Strang): https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
10. Gajendra Purohit linear algebra for IIT JAM (Unacademy): https://unacademy.com/course/detailed-course-on-linear-algebra---iit-jam,-2024/KK0CIVPR
11. NPTEL Real Analysis I (IIT Palakkad): https://onlinecourses.nptel.ac.in/noc20_ma51/preview · Basic Real Analysis: https://archive.nptel.ac.in/noc/courses/noc22/SEM1/noc22-ma05
12. JAM 2026 previous papers: https://jam2026.iitb.ac.in/oldQP.html
13. JAM 2026 MS paper and key: https://jam2026.iitb.ac.in/qpnkey26.html
14. JAM 2026 mock test page: https://jam2026.iitb.ac.in/mockTest.html
15. JAM 2027 (IIT KGP): https://jam.iitkgp.ac.in/ · https://jam.iitkgp.ac.in/notifications.html
16. Mainack Paul, AIR 2, JAM MS 2021 (Cheenta): https://cheenta.com/?p=89201
17. Unacademy free class, JAM MS 2026 discussion: https://unacademy.com/class/jam-ms-2026-discussion-part-2/1EUMN9EE
18. Cheenta, JAM MS 2021 solutions: https://cheenta.com/iit-jam-statistics-2021-paper-set-b-problem-solutions/
19. Unacademy All India Mock Test, MS 2026: https://unacademy.com/test-series/all-india-mock-test-for-iit-jam-2026-statistics/TW44AGB0
20. Vaishnavi Jaiswal, AIR 4, JAM MS 2021 (Cheenta): https://cheenta.com/how-vaishnavi-jaiswal-got-air-4-in-iit-jam-ms-2021/
21. MIT 6.041 (Fall 2010 lecture videos): https://ocw.mit.edu/courses/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/video_galleries/lecture-videos
22. Pishro-Nik, Introduction to Probability, Statistics and Random Processes (free): https://www.probabilitycourse.com/
23. Grinstead & Snell, Introduction to Probability (GNU FDL): https://math.dartmouth.edu/~prob/prob/prob.pdf
24. NPTEL Intro to Probability Theory and Stochastic Processes (Dharmaraja): https://onlinecourses.nptel.ac.in/noc24_ma97/preview
25. NPTEL Non-Parametric Statistical Inference: https://onlinecourses.nptel.ac.in/noc25_ma63/preview · https://onlinecourses.nptel.ac.in/noc20_ma55/preview
26. PW, JAM 2026 AIR 11 MS topper: https://www.pw.live/iit-jam/exams/iit-jam-2026-air-11-mathematical-statistics-topper-yogesh-kumar-strategy-and-success-story
27. Price snapshots: https://www.flipkart.com/fundamentals-mathematical-statistics-paperback-s-c-gupta-v-k-kapoor/p/itme2b4c7d1e5327 · https://retailmaharaj.com/products/introduction-to-mathematical-statistics-8e

#!/usr/bin/env python3
"""Build the small, static public front door for the study archive."""

from __future__ import annotations

from datetime import date
from html import escape
from pathlib import Path
import shutil
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "_site"
REPOSITORY = "https://github.com/damminhtien/mit-micromasters-program-in-statistics-and-data-science"
PAGES_URL = "https://damminhtien.github.io/mit-micromasters-program-in-statistics-and-data-science/"

COURSES = [
    {
        "slug": "probability",
        "code": "6.431x",
        "title": "Probability",
        "kind": "Core course",
        "summary": "A rigorous path from probability models and conditioning to stochastic processes and Markov chains.",
        "source": "6.431x_probability/README.md",
        "notes": "6.431x_probability/study_notes/README.md",
        "focus": ["Conditioning and Bayes", "Random variables and expectations", "Limit theorems", "Markov chains"],
        "status": "All ten units have local entry points; depth remains intentionally uneven.",
    },
    {
        "slug": "statistics",
        "code": "18.6501x",
        "title": "Fundamentals of Statistics",
        "kind": "Core course",
        "summary": "Mathematical statistics with a focus on estimators, testing, Bayesian reasoning, and model assumptions.",
        "source": "18.6501x_statistics/README.md",
        "notes": "18.6501x_statistics/study_notes/README.md",
        "focus": ["Estimation and MLE", "Parametric and nonparametric tests", "Confidence and uncertainty", "Bayesian statistics"],
        "status": "Units one to six are mapped locally; Units 3–4 include source-grounded summaries.",
    },
    {
        "slug": "machine-learning",
        "code": "6.86x",
        "title": "Machine Learning with Python",
        "kind": "Core course",
        "summary": "From linear classifiers and regularization to kernels, recommender systems, and neural networks.",
        "source": "6.86x_machinelearning/README.md",
        "notes": "6.86x_machinelearning/study_notes/README.md",
        "focus": ["Generalization and regularization", "Nonlinear and kernel methods", "Recommender systems", "Neural networks"],
        "status": "Selected lecture assets, notes, projects, and runnable baselines are included.",
    },
    {
        "slug": "data-analysis",
        "code": "6.419x",
        "title": "Data Analysis",
        "kind": "Elective",
        "summary": "Statistical modeling and computation across high-dimensional data, networks, time series, and applications.",
        "source": "6.419x_dataanalysis/README.md",
        "notes": "6.419x_dataanalysis/study_notes/README.md",
        "focus": ["High-dimensional classification and clustering", "Network analysis", "Time series", "Written analytical reports"],
        "status": "Modules 0–3 have local material; Gaussian-process coverage remains primarily external.",
    },
]

PROJECTS = [
    {
        "title": "Matrix completion and recommendation",
        "tag": "Algorithms",
        "summary": "Gaussian-mixture EM, K-means baseline, BIC model selection, and matrix filling on bundled toy data.",
        "entry": "6.86x_machinelearning/projects/project4_netflix/main.py",
        "folder": "6.86x_machinelearning/projects/project4_netflix/",
        "status": "Smoke-tested",
    },
    {
        "title": "Sentiment classification",
        "tag": "Classical ML",
        "summary": "Bag-of-words features, perceptron variants, Pegasos, and a small correctness harness.",
        "entry": "6.86x_machinelearning/projects/sentiment_analysis/project1.py",
        "folder": "6.86x_machinelearning/projects/sentiment_analysis/",
        "status": "Harness passes",
    },
    {
        "title": "MNIST model baselines",
        "tag": "Deep learning",
        "summary": "PCA, softmax regression, fully connected networks, and convolutional models in a readable progression.",
        "entry": "6.86x_machinelearning/projects/mnist/part1/softmax.py",
        "folder": "6.86x_machinelearning/projects/mnist/",
        "status": "Educational reference",
    },
    {
        "title": "High-dimensional analysis",
        "tag": "Data analysis",
        "summary": "A notebook workflow from transformation and PCA to visualization, clustering, and feature selection.",
        "entry": "6.419x_dataanalysis/projects/Analysis1.ipynb",
        "folder": "6.419x_dataanalysis/projects/",
        "status": "Dataset-dependent",
    },
    {
        "title": "CAVIAR network analysis",
        "tag": "Networks",
        "summary": "Phase-by-phase network exploration backed by bundled intervention CSVs.",
        "entry": "6.419x_dataanalysis/projects/Analysis3_1.ipynb",
        "folder": "6.419x_dataanalysis/projects/",
        "status": "Bundled phases",
    },
]


def github_url(path: str, tree: bool = False) -> str:
    kind = "tree" if tree else "blob"
    return f"{REPOSITORY}/{kind}/main/{quote(path, safe='/')}"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def nav(active: str) -> str:
    links = [
        ("Home", "index.html", "home"),
        ("Courses", "courses.html", "courses"),
        ("Projects", "projects.html", "projects"),
        ("Showcases", "showcases.html", "showcases"),
    ]
    items = []
    for label, href, key in links:
        current = ' aria-current="page"' if active == key else ""
        items.append(f'<a href="{href}"{current}>{label}</a>')
    return "".join(items)


def layout(title: str, description: str, body: str, active: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{escape(description)}">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:type" content="website">
  <link rel="stylesheet" href="assets/site.css">
  <title>{escape(title)} · MITx SDS Study Hub</title>
</head>
<body>
  <div class="shell">
    <header class="site-header">
      <a class="brand" href="index.html"><span class="brand-mark">SDS</span><span>MITx study hub</span></a>
      <nav aria-label="Primary navigation">{nav(active)}</nav>
    </header>
    <main>{body}</main>
    <footer>
      <span>Independent learner archive · refreshed {date.today().isoformat()}</span>
      <span><a href="{REPOSITORY}">Source on GitHub</a> · <a href="{REPOSITORY}/blob/main/docs/PROVENANCE.md">Provenance</a></span>
    </footer>
  </div>
</body>
</html>
"""


def button(label: str, href: str, secondary: bool = False) -> str:
    cls = "button secondary" if secondary else "button"
    return f'<a class="{cls}" href="{href}">{escape(label)}</a>'


def course_card(course: dict[str, object]) -> str:
    focus = "".join(f"<li>{escape(item)}</li>" for item in course["focus"])
    return f"""
    <article class="card course-card">
      <div class="card-top"><span class="eyebrow">{escape(str(course["kind"]))}</span><span class="course-code">{escape(str(course["code"]))}</span></div>
      <h3>{escape(str(course["title"]))}</h3>
      <p>{escape(str(course["summary"]))}</p>
      <ul class="compact-list">{focus}</ul>
      <div class="card-actions">
        {button("Course map", f'course-{course["slug"]}.html')}
        {button("Source README", github_url(str(course["source"])), True)}
      </div>
    </article>
    """


def project_card(project: dict[str, str]) -> str:
    return f"""
    <article class="card project-card">
      <div class="card-top"><span class="eyebrow">{escape(project["tag"])}</span><span class="status">{escape(project["status"])}</span></div>
      <h3>{escape(project["title"])}</h3>
      <p>{escape(project["summary"])}</p>
      <div class="card-actions">
        {button("Open entry point", github_url(project["entry"]))}
        {button("Browse project", github_url(project["folder"], tree=True), True)}
      </div>
    </article>
    """


def build_home() -> None:
    courses = "".join(course_card(course) for course in COURSES)
    projects = "".join(project_card(project) for project in PROJECTS[:3])
    body = f"""
    <section class="hero">
      <div class="hero-copy">
        <p class="eyebrow">MITx MicroMasters in Statistics and Data Science</p>
        <h1>A clearer route through a demanding program.</h1>
        <p class="lede">A learner-maintained archive of course maps, source-aware notes, reusable projects, and personal learning milestones.</p>
        <div class="hero-actions">
          {button("Explore the courses", "courses.html")}
          {button("Browse reusable projects", "projects.html", True)}
        </div>
        <div class="trust-row"><span>Source-aware</span><span>Reproducibility-minded</span><span>Publicly redacted</span></div>
      </div>
      <div class="hero-panel">
        <span class="panel-label">Start with the signal</span>
        <strong>4</strong>
        <span>local course hubs</span>
        <div class="mini-rule"></div>
        <strong>5</strong>
        <span>reusable project entry points</span>
        <div class="mini-rule"></div>
        <strong>1</strong>
        <span>content-quality gate for local links</span>
      </div>
    </section>

    <section class="section intro-grid">
      <div>
        <p class="eyebrow">Why this archive exists</p>
        <h2>Find the concept. Inspect the implementation. Know the boundary.</h2>
      </div>
      <p>This public front door separates course-derived learning material from personal showcases and third-party references. Each course page points back to the full repository, where assumptions, data requirements, and provenance stay visible.</p>
    </section>

    <section class="section">
      <div class="section-heading"><div><p class="eyebrow">Course map</p><h2>Four ways in</h2></div><a class="text-link" href="courses.html">View all courses →</a></div>
      <div class="card-grid">{courses}</div>
    </section>

    <section class="section tinted">
      <div class="section-heading"><div><p class="eyebrow">Reusable work</p><h2>Projects people can build on</h2></div><a class="text-link" href="projects.html">Open project gallery →</a></div>
      <div class="card-grid">{projects}</div>
    </section>

    <section class="section showcase-strip">
      <div>
        <p class="eyebrow">Learning journey</p>
        <h2>The work stays personal. The useful parts stay discoverable.</h2>
        <p>Selected reports, program context, and redacted milestones are preserved as showcases while the reusable code and notebooks remain the main entry point.</p>
        {button("See the showcases", "showcases.html")}
      </div>
      <img src="assets/images/mitx_sds.png" alt="MITx Statistics and Data Science program visual">
    </section>

    <section class="section callout">
      <p class="eyebrow">Read responsibly</p>
      <p>Independent learner work is not official MIT or edX material. Course links may require authentication, and datasets or exported assets may have redistribution limits.</p>
      <a class="text-link" href="{REPOSITORY}/blob/main/docs/QUALITY.md">Read the quality policy →</a>
    </section>
    """
    write(OUT / "index.html", layout("Home", "A curated public front door for the MITx SDS learner archive.", body, "home"))


def build_courses() -> None:
    cards = "".join(course_card(course) for course in COURSES)
    body = f"""
    <section class="page-heading">
      <p class="eyebrow">Course map</p>
      <h1>Learn by route, not by folder name.</h1>
      <p class="lede">The archive covers three core courses and one local elective. The pages below give each route a human-readable entry point and state its current coverage honestly.</p>
    </section>
    <section class="card-grid">{cards}</section>
    <section class="section callout">
      <p class="eyebrow">Program context</p>
      <p>The current credential structure and eligibility rules can change. Use the official MIT SDS site for policy, dates, and enrollment information.</p>
      <a class="text-link" href="https://micromasters.mit.edu/ds/">Open official MIT SDS site →</a>
    </section>
    """
    write(OUT / "courses.html", layout("Courses", "Course maps for Probability, Statistics, Machine Learning, and Data Analysis.", body, "courses"))


def build_course_page(course: dict[str, object]) -> None:
    focus = "".join(f"<li>{escape(item)}</li>" for item in course["focus"])
    body = f"""
    <section class="page-heading">
      <p class="eyebrow">{escape(str(course["kind"]))} · {escape(str(course["code"]))}</p>
      <h1>{escape(str(course["title"]))}</h1>
      <p class="lede">{escape(str(course["summary"]))}</p>
      <div class="hero-actions">
        {button("Open full course README", github_url(str(course["source"])))}
        {button("Open study-notes index", github_url(str(course["notes"])), True)}
      </div>
    </section>
    <section class="detail-grid">
      <article class="card">
        <p class="eyebrow">Study focus</p>
        <h2>What to look for</h2>
        <ul class="feature-list">{focus}</ul>
      </article>
      <article class="card">
        <p class="eyebrow">Coverage boundary</p>
        <h2>What is here now</h2>
        <p>{escape(str(course["status"]))}</p>
        <p class="muted">The full source tree remains the canonical reading surface; this page is a curated map, not a replacement syllabus.</p>
      </article>
    </section>
    <section class="section callout">
      <p class="eyebrow">Keep context visible</p>
      <p>Check the local provenance and quality notes before redistributing course assets or treating a learner-authored derivation as an official solution.</p>
      <a class="text-link" href="{REPOSITORY}/blob/main/docs/PROVENANCE.md">Open provenance guide →</a>
    </section>
    """
    write(OUT / f'course-{course["slug"]}.html', layout(str(course["title"]), str(course["summary"]), body, "courses"))


def build_projects() -> None:
    cards = "".join(project_card(project) for project in PROJECTS)
    body = f"""
    <section class="page-heading">
      <p class="eyebrow">Reusable project gallery</p>
      <h1>Small artifacts with a clear next step.</h1>
      <p class="lede">These projects are course-derived educational artifacts. Open an entry point, read the assumptions, then adapt the smallest working example.</p>
    </section>
    <section class="card-grid">{cards}</section>
    <section class="section callout">
      <p class="eyebrow">A safer reuse loop</p>
      <p>Read the project README, install the shared baseline, run the toy or correctness check, then replace data only after checking the schema and license.</p>
      <a class="text-link" href="{REPOSITORY}/blob/main/docs/PROJECTS.md">Read the detailed project runbook →</a>
    </section>
    """
    write(OUT / "projects.html", layout("Projects", "Reusable algorithms, notebooks, datasets, and project runbooks.", body, "projects"))


def build_showcases() -> None:
    body = f"""
    <section class="page-heading">
      <p class="eyebrow">Learning journey showcases</p>
      <h1>The story behind the study archive.</h1>
      <p class="lede">Personal milestones and reports are preserved here with explicit context. Reusable code and notebooks stay in the project gallery.</p>
    </section>
    <section class="showcase-grid">
      <figure class="showcase-card wide"><img src="assets/images/mitx_sds.png" alt="MITx Statistics and Data Science program visual"><figcaption><strong>Program context</strong><span>Use the official MIT SDS site for current policy and dates.</span></figcaption></figure>
      <figure class="showcase-card"><img src="assets/images/letter_public.png" alt="Redacted MIT IDSS program letter"><figcaption><strong>Program letter</strong><span>Owner-provided milestone with personal identifiers redacted.</span></figcaption></figure>
      <figure class="showcase-card"><img src="assets/images/cert_public.png" alt="Redacted MITx SDS completion certificate"><figcaption><strong>Certificate</strong><span>Owner-provided completion milestone with identifying fields redacted.</span></figcaption></figure>
      <figure class="showcase-card wide"><img src="assets/images/written_report.drawio.png" alt="Written report workflow artifact"><figcaption><strong>Written report artifact</strong><span>A visual reminder that the reports are learner work, not official solutions.</span></figcaption></figure>
    </section>
    <section class="section callout">
      <p class="eyebrow">Boundary</p>
      <p>The original private images are not tracked. This public build copies only the redacted derivatives and other non-sensitive visuals.</p>
      <a class="text-link" href="{REPOSITORY}/blob/main/docs/SHOWCASES.md">Open showcase provenance →</a>
    </section>
    """
    write(OUT / "showcases.html", layout("Showcases", "Personal learning milestones and reports with explicit provenance.", body, "showcases"))


def build_404() -> None:
    body = """
    <section class="page-heading centered">
      <p class="eyebrow">404</p>
      <h1>This route wandered off.</h1>
      <p class="lede">Return to the study hub or browse the course map.</p>
      <div class="hero-actions"><a class="button" href="index.html">Back home</a><a class="button secondary" href="courses.html">View courses</a></div>
    </section>
    """
    write(OUT / "404.html", layout("Page not found", "The requested study hub page was not found.", body, "home"))


def copy_public_assets() -> None:
    assets = OUT / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "web" / "site.css", assets / "site.css")
    image_dir = assets / "images"
    image_dir.mkdir(parents=True, exist_ok=True)
    for filename in ("mitx_sds.png", "written_report.drawio.png", "letter_public.png", "cert_public.png"):
        source = ROOT / "resources" / "images" / filename
        if not source.exists():
            raise FileNotFoundError(f"Missing public site asset: {source}")
        shutil.copy2(source, image_dir / filename)


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    copy_public_assets()
    (OUT / ".nojekyll").touch()
    build_home()
    build_courses()
    for course in COURSES:
        build_course_page(course)
    build_projects()
    build_showcases()
    build_404()
    write(OUT / "robots.txt", f"User-agent: *\nAllow: /\nSitemap: {PAGES_URL}sitemap.xml\n")
    write(OUT / "sitemap.xml", f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>{PAGES_URL}</loc></url>
  <url><loc>{PAGES_URL}courses.html</loc></url>
  <url><loc>{PAGES_URL}projects.html</loc></url>
  <url><loc>{PAGES_URL}showcases.html</loc></url>
</urlset>
""")
    print(f"built {len(list(OUT.rglob('*')))} site files in {OUT}")


if __name__ == "__main__":
    main()

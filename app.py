import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import pymupdf
import base64
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

PROJECT_IMAGES = {
    "mmm": BASE_DIR / "assets" / "images" / "mmm.png",
    "vehicle": BASE_DIR / "assets" / "images" / "vehicle.png",
    "rag": BASE_DIR / "assets" / "images" / "rag.png",
}



# =========================================================
# PROJECT IMAGES
# =========================================================





ASSET_DIR = Path(__file__).resolve().parent / "assets" / "images"
PROJECT_IMAGE_FILES = {
    "mmm": ASSET_DIR / "mmm.png",
    "vehicle": ASSET_DIR / "vehicle.png",
    "rag": ASSET_DIR / "rag.png",
}

def image_data_uri(path):
    """Return a browser-safe data URI for a local project image."""
    if not path.exists() or path.stat().st_size == 0:
        return ""
    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:image/png;base64,{encoded}"

PROJECT_IMAGES = {
    key: image_data_uri(path)
    for key, path in PROJECT_IMAGE_FILES.items()
}

# Resume preview is rendered as an image using PyMuPDF.
# This works across Streamlit versions and avoids Chrome PDF iframe blocking.

# =========================================================
# RESUME FILE
# =========================================================
RESUME_PATH = Path(__file__).resolve().parent / "resume.pdf"
RESUME_EXISTS = RESUME_PATH.exists() and RESUME_PATH.stat().st_size > 0
RESUME_DATA = RESUME_PATH.read_bytes() if RESUME_EXISTS else b""

# =========================================================
# PROJECT GITHUB REPOSITORIES
# =========================================================
# Replace these placeholder URLs with your actual GitHub
# repository URLs. The buttons are ready to use.
PROJECT_REPOS = {
    "mmm": "https://github.com/",
    "vehicle": "https://github.com/kumarakshay7/Annotation",
    "rag": "https://github.com/kumarakshay7/Azure-RAG-Assignment",
}

# =========================================================
# RESUME PREVIEW
# =========================================================
if "show_resume_preview" not in st.session_state:
    st.session_state.show_resume_preview = False

def show_resume_preview():
    if not RESUME_EXISTS:
        st.error("Resume PDF not found. Put a valid non-empty file named 'resume.pdf' next to app.py.")
        return

    st.session_state.show_resume_preview = True


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Akshay Kumar | Data Analyst",
    page_icon="📊",
    layout="wide"
)

if not RESUME_EXISTS:
    st.warning("Resume PDF not found. Put a valid non-empty file named 'resume.pdf' next to app.py.")


# =========================================================
# CUSTOM CSS
# =========================================================


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');

:root {
    --bg: #08090b;
    --panel: #10141b;
    --panel-2: #0c0f14;
    --line: #1b2330;
    --line-soft: #151b24;
    --text: #f7f9fc;
    --muted: #91a6c0;
    --muted-2: #7f94ad;
    --blue: #3d86ff;
    --blue-bright: #19cfff;
}

html { scroll-behavior: smooth; }

.stApp {
    background:
        linear-gradient(rgba(255,255,255,.018) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,.018) 1px, transparent 1px),
        var(--bg);
    background-size: 72px 72px;
    color: var(--text);
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1400px;
    padding-top: 0.7rem;
    padding-bottom: 0;
}

#MainMenu, footer, header { visibility: hidden; }

/* ========================= NAV ========================= */
.nav-shell {
    min-height: 64px;
    border-bottom: 1px solid rgba(255,255,255,.045);
    display: flex;
    align-items: center;
}
.nav-logo {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 23px;
    font-weight: 700;
    color: #fff;
    padding-top: 3px;
}
.nav-logo span { color: var(--blue); }

.nav-item {
    text-align: center;
    padding-top: 11px;
    font-size: 14px;
    font-weight: 500;
}
.nav-item a {
    color: #8fa0b7;
    text-decoration: none;
    transition: .2s ease;
}
.nav-item a:hover { color: #fff; }

.nav-button button {
    min-height: 40px !important;
    height: 40px !important;
    border-radius: 8px !important;
    padding: 0 15px !important;
    background: #10141b !important;
    color: #d8e4f3 !important;
    border: 1px solid #1d2634 !important;
}
.nav-button button:hover {
    border-color: #3d86ff !important;
    color: #fff !important;
}

/* ========================= HERO ========================= */
.hero-space { height: 125px; }

.hero-grid {
    min-height: 720px;
}

.eyebrow {
    color: #8ca5c4;
    letter-spacing: 4px;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    margin-bottom: 24px;
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(52px, 5vw, 72px);
    line-height: 1.02;
    font-weight: 700;
    letter-spacing: -2.8px;
    color: #fff;
}

.hero-subtitle {
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(30px, 3vw, 40px);
    line-height: 1.12;
    font-weight: 600;
    letter-spacing: -1.5px;
    color: #91a6c0;
    margin-top: 17px;
}

.hero-text {
    color: #91a6c0;
    font-size: 17px;
    line-height: 1.85;
    max-width: 760px;
    margin-top: 25px;
}

.hero-actions {
    margin-top: 32px;
    width: 100%;
}

.hero-actions [data-testid="column"] {
    display: flex;
    align-items: stretch;
}

.hero-actions button,
.hero-actions a {
    width: 100% !important;
    min-height: 48px !important;
    height: 48px !important;
    border-radius: 7px !important;
    box-sizing: border-box !important;
}

.hero-actions .stButton,
.hero-actions .stDownloadButton,
.hero-actions .stLinkButton {
    width: 100% !important;
}

.hero-actions .project-view-button {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 0 12px !important;
    margin: 0 !important;
}

.hero-actions .hero-icon button {
    min-width: 48px !important;
    padding: 0 10px !important;
    font-size: 17px !important;
}

.primary-button button {
    background: var(--blue) !important;
    color: #fff !important;
    border-color: var(--blue) !important;
    font-weight: 700 !important;
}
.primary-button button:hover {
    background: #2f74e7 !important;
}

.hero-icon button {
    min-width: 48px !important;
    padding: 0 10px !important;
    font-size: 17px !important;
}

.location {
    color: #7f94ad;
    margin-top: 35px;
    font-size: 15px;
}

/* ========================= IMPACT ========================= */
.impact-card {
    position: relative;
    background: #10141b;
    border: 1px solid #202938;
    border-radius: 12px;
    padding: 34px 36px 36px;
    min-height: 625px;
    overflow: hidden;
    box-shadow: 0 18px 50px rgba(0,0,0,.16);
}

.impact-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
    z-index: 3;
}

.impact-label {
    color: #8ca5c4;
    letter-spacing: 4px;
    font-size: 12px;
    font-weight: 600;
}

.impact-growth {
    color: #00c9f5;
    font-size: 13px;
    font-weight: 700;
}

.impact-title {
    color: #ffffff;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 34px;
    line-height: 1.1;
    font-weight: 700;
    margin-top: 10px;
    letter-spacing: -1px;
    position: relative;
    z-index: 3;
}

/* CSS-only chart. No SVG, JavaScript or Plotly is used here. */
.impact-chart {
    position: relative;
    height: 260px;
    margin: 18px 0 10px;
    overflow: hidden;
}

.impact-chart-grid {
    position: absolute;
    inset: 0;
    opacity: .48;
    background-image:
        linear-gradient(rgba(49,63,82,.32) 1px, transparent 1px),
        linear-gradient(90deg, rgba(49,63,82,.25) 1px, transparent 1px);
    background-size: 25% 25%;
}

.impact-chart-area {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    height: 78%;
    background: linear-gradient(
        to bottom,
        rgba(61,134,255,.18),
        rgba(61,134,255,.015)
    );
    clip-path: polygon(
        0% 70%,
        8% 62%,
        16% 66%,
        25% 49%,
        34% 40%,
        42% 45%,
        51% 30%,
        60% 18%,
        68% 24%,
        76% 8%,
        84% -1%,
        92% -10%,
        100% -20%,
        100% 100%,
        0% 100%
    );
}

.impact-chart-line {
    position: absolute;
    inset: 0;
    z-index: 2;
}

/* Individual line segments create the smooth rising trend without SVG. */
.impact-chart-line span {
    position: absolute;
    height: 3px;
    background: #3d86ff;
    border-radius: 999px;
    transform-origin: left center;
    box-shadow: 0 0 8px rgba(61,134,255,.18);
}

.chart-seg-1 { left: 0%;  top: 70%; width: 9%;  transform: rotate(-12deg); }
.chart-seg-2 { left: 8%;  top: 62%; width: 9%;  transform: rotate(5deg); }
.chart-seg-3 { left: 16%; top: 66%; width: 11%; transform: rotate(-24deg); }
.chart-seg-4 { left: 25%; top: 49%; width: 10%; transform: rotate(-13deg); }
.chart-seg-5 { left: 34%; top: 40%; width: 9%;  transform: rotate(8deg); }
.chart-seg-6 { left: 42%; top: 45%; width: 11%; transform: rotate(-29deg); }
.chart-seg-7 { left: 51%; top: 30%; width: 11%; transform: rotate(-14deg); }
.chart-seg-8 { left: 60%; top: 18%; width: 9%;  transform: rotate(9deg); }
.chart-seg-9 { left: 68%; top: 24%; width: 10%; transform: rotate(-26deg); }
.chart-seg-10 { left: 76%; top: 8%; width: 11%; transform: rotate(-14deg); }
.chart-seg-11 { left: 84%; top: -1%; width: 10%; transform: rotate(-13deg); }
.chart-seg-12 { left: 92%; top: -10%; width: 10%; transform: rotate(-13deg); }

.impact-metrics {
    position: relative;
    z-index: 3;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
}

.metric-box {
    background: #0a0d12;
    border: 1px solid #151d2a;
    border-radius: 8px;
    padding: 18px 17px;
    min-height: 76px;
}

.metric-number {
    color: #3d86ff;
    font-size: 24px;
    font-weight: 800;
    line-height: 1.1;
}

.metric-label {
    color: #91a6c0;
    font-size: 13px;
    margin-top: 8px;
}

@media (max-width: 900px) {
    .impact-card {
        min-height: auto;
        padding: 28px 24px 26px;
    }

    .impact-title {
        font-size: 30px;
    }

    .impact-chart {
        height: 220px;
    }
}



/* ========================= GENERAL SECTIONS ========================= */
.section {
    margin-top: 90px;
    margin-bottom: 20px;
}
.section-label {
    color: #8ca5c4;
    letter-spacing: 4px;
    font-size: 12px;
    font-weight: 600;
}
.section-title {
    font-family: 'Space Grotesk', sans-serif;
    color: #fff;
    font-size: 43px;
    font-weight: 700;
    letter-spacing: -1.5px;
    margin-top: 12px;
}
.section-description {
    color: #91a6c0;
    font-size: 17px;
    line-height: 1.7;
    max-width: 850px;
}

/* ========================= CARDS ========================= */
.project-card, .experience-card, .skill-card, .cert-card {
    background: #0c0f14;
    border: 1px solid #1b2330;
    border-radius: 10px;
    padding: 28px;
}
.project-card {
    width: 100%;
    min-height: 0;
    margin: 0 auto 34px auto;
    padding: 0 0 28px 0;
    overflow: hidden;
    background: linear-gradient(180deg, #0c1118 0%, #090d13 100%);
    border: 1px solid #1b2a3d;
    border-radius: 14px;
    transition: transform .25s ease, border-color .25s ease, box-shadow .25s ease;
}
.project-card:hover {
    transform: translateY(-4px);
    border-color: #315eae;
    box-shadow: 0 18px 50px rgba(0,0,0,.28);
}
.project-card:hover, .experience-card:hover, .skill-card:hover, .cert-card:hover {
    border-color: #315eae;
}
.project-title, .experience-title {
    color: #fff;
    font-weight: 700;
}
.project-title { font-size: 25px; }
.project-index {
    color: #FFD700;
    font-weight: 800;
    font-size: 15px;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 18px;
}
.project-tech { color: var(--blue); font-weight: 600; margin-top: 8px; }

.project-repo {
    margin-top: 22px;
}
.project-repo a {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    text-decoration: none !important;
    color: #dce8f7 !important;
    border: 1px solid #26364d;
    background: #111721;
    border-radius: 7px;
    padding: 9px 14px;
    font-weight: 600;
    transition: all .2s ease;
}
.project-repo a:hover {
    color: #ffffff !important;
    border-color: #3d86ff;
    background: #151d29;
}
 .project-image-wrap {
    position: relative;
    overflow: hidden;
    width: 100%;
    height: 560px;
    margin: 0 0 28px 0;
    border-radius: 14px 14px 0 0;
    background:
        radial-gradient(circle at 50% 20%, rgba(61,134,255,.10), transparent 45%),
        #080c12;
    border-bottom: 1px solid #1b2330;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 8px 10px;
    box-sizing: border-box;
}
.project-image-wrap img {
    width: 100%;
    height: 100%;
    display: block;
    object-fit: contain;
    object-position: center;
    border-radius: 8px;
    transition: transform .35s ease, filter .35s ease;
}
.project-image-wrap:hover img {
    transform: scale(1.025);
    filter: brightness(1.08);
}
.project-image-overlay {
    position: absolute;
    left: 14px;
    bottom: 12px;
    padding: 6px 10px;
    border: 1px solid rgba(255,255,255,.16);
    border-radius: 6px;
    background: rgba(7,10,15,.78);
    color: #dce8f7;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    backdrop-filter: blur(8px);
}
.project-card-body {
    padding: 0 34px;
}
.project-card-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    margin-bottom: 10px;
}
.project-card-description {
    color: #91a5bd;
    font-size: 16px;
    line-height: 1.8;
    max-width: 1050px;
    margin-top: 18px;
}
.project-metric-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
    margin-top: 24px;
}
.project-metric {
    min-height: 82px;
    padding: 14px 16px;
    border: 1px solid #1b2a3d;
    border-radius: 9px;
    background: #090e15;
}
.project-metric-value {
    color: #3d86ff;
    font-size: 22px;
    font-weight: 800;
}
.project-metric-label {
    color: #849ab4;
    font-size: 13px;
    margin-top: 5px;
}
.project-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 18px;
}
.project-tag {
    display: inline-flex;
    align-items: center;
    padding: 6px 10px;
    border: 1px solid #26364d;
    border-radius: 7px;
    background: #0e151f;
    color: #a8bbd1;
    font-size: 12px;
}
@media (max-width: 800px) {
    .project-image-wrap { height: 460px; padding: 6px; }
    .project-card-body { padding: 0 20px; }
    .project-metric-grid { grid-template-columns: 1fr; }
}

.project-image-placeholder {
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #607894;
    font-size: 13px;
    letter-spacing: 1px;
}
.project-description, .experience-text {
    color: #91a6c0;
    line-height: 1.75;
    margin-top: 20px;
}
.tag {
    display: inline-block;
    background: #111721;
    border: 1px solid #202d40;
    border-radius: 5px;
    color: #9bb2cf;
    font-size: 12px;
    padding: 7px 10px;
    margin: 4px 3px 4px 0;
}
.experience-card { margin-bottom: 25px; }
.experience-date { color: var(--blue); font-weight: 700; font-size: 17px; }
.experience-location { color: #7f94ad; margin-top: 7px; }
.experience-title { font-size: 25px; margin-top: 20px; }
.experience-company { color: #91a6c0; font-size: 17px; margin-top: 5px; }
.skill-title { color: #fff; font-size: 21px; font-weight: 700; margin-bottom: 18px; }
.cert-card { min-height: 180px; }
.cert-title { color: #fff; font-size: 18px; font-weight: 700; }
.cert-provider { color: var(--blue); margin-top: 15px; }

.contact-text { color: #91a6c0; font-size: 17px; line-height: 1.8; }
.contact-title {
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 5px;
    color: #9bb6d5;
    margin-top: 5px;
    margin-bottom: 25px;
}
.contact-card {
    background: #10141b;
    border: 1px solid #202938;
    border-radius: 12px;
    padding: 30px;
}
.footer {
    margin-top: 100px;
    padding: 35px;
    border-top: 1px solid #151b24;
    text-align: center;
    color: #71839a;
}

div.stButton > button, .stLinkButton > a, div[data-testid="stDownloadButton"] > button {
    border-radius: 7px !important;
    font-weight: 600 !important;
}

div[data-testid="stDownloadButton"] > button { width: 100% !important; }

.resume-preview {\n    scroll-margin-top: 80px;
    background: #10141b;
    border: 1px solid #202938;
    border-radius: 10px;
    padding: 14px;
    margin: 18px 0 8px 0;
}
#projects { scroll-margin-top: 90px; }\n\n.project-view-button {
    display: inline-block;
    width: 100%;
    box-sizing: border-box;
    text-align: center;
    text-decoration: none !important;
    background: transparent;
    color: #d8e4f3 !important;
    border: 1px solid #2b3a50;
    border-radius: 7px;
    padding: 9px 12px;
    font-weight: 600;
}
.project-view-button:hover {
    color: #fff !important;
    border-color: #3d86ff;
    background: rgba(61,134,255,.08);
}
.primary-button div[data-testid="stDownloadButton"] > button {
    background: var(--blue) !important; color: #fff !important;
    border: 1px solid var(--blue) !important; font-weight: 700 !important;
}
.primary-button div[data-testid="stDownloadButton"] > button:hover {
    background: #2f74e7 !important; border-color: #2f74e7 !important;
}
.nav-button div[data-testid="stDownloadButton"] > button {
    min-height: 40px !important; height: 40px !important; border-radius: 8px !important;
    padding: 0 15px !important; background: #10141b !important;
    color: #d8e4f3 !important; border: 1px solid #1d2634 !important;
}

@media (max-width: 900px) {
    .hero-space { height: 65px; }
    .hero-title { font-size: 48px; }
    .hero-subtitle { font-size: 28px; }
    .section-title, .contact-title { font-size: 34px; }
    .impact-card { margin-top: 35px; }
}
@media (max-width: 600px) {
    .hero-title { font-size: 40px; letter-spacing: -1.5px; }
    .hero-subtitle { font-size: 25px; }
    .impact-title { font-size: 29px; }
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# NAVIGATION
# =========================================================

st.markdown(
    '<div class="nav-shell"></div>',
    unsafe_allow_html=True
)

nav1, nav2, nav3, nav4, nav5, nav6 = st.columns(
    [2.3, 1, 1, 1, 1, 0.8],
    gap="small"
)

with nav1:
    st.markdown(
        '<div class="nav-logo">AK<span>.</span></div>',
        unsafe_allow_html=True
    )

with nav2:
    st.markdown(
        '<div class="nav-item"><a href="#projects">Projects</a></div>',
        unsafe_allow_html=True
    )

with nav3:
    st.markdown(
        '<div class="nav-item"><a href="#experience">Experience</a></div>',
        unsafe_allow_html=True
    )

with nav4:
    st.markdown(
        '<div class="nav-item"><a href="#skills">Skills</a></div>',
        unsafe_allow_html=True
    )

with nav5:
    st.markdown(
        '<div class="nav-item"><a href="#certifications">Certifications</a></div>',
        unsafe_allow_html=True
    )

with nav6:
    st.markdown(
        '<div class="nav-item"><a href="#contact">Contact</a></div>',
        unsafe_allow_html=True
    )


# =========================================================
# HERO
# =========================================================

st.markdown(
    '<div class="hero-space"></div>',
    unsafe_allow_html=True
)

hero_left, hero_right = st.columns(
    [1.28, 0.72],
    gap="large"
)

# =========================================================
# LEFT SIDE
# =========================================================

with hero_left:

    st.markdown("""
    <div class="eyebrow">
        DATA ANALYST · MACHINE LEARNING · GENAI · MARKETING ANALYTICS
    </div>
    <div class="hero-title">Akshay Kumar</div>
    <div class="hero-subtitle">Data that decides. Models that deliver.</div>
    <div class="hero-text">
        I turn raw data into decisions using regression models, computer vision,
        and RAG-powered AI assistants that measurably lift ROI.
    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # HERO ACTION BUTTONS
    # =====================================================

    st.markdown(
        '<div class="hero-actions">',
        unsafe_allow_html=True
    )

    action1, action2, action3, action4, action5, action6 = st.columns(
        [1.25, 1.25, 1.05, 0.32, 0.32, 0.32],
        gap="small"
    )

    with action1:
        if st.button(
            "⇩  View Resume",
            disabled=not RESUME_EXISTS,
            use_container_width=True,
            key="hero_resume_preview",
        ):
            st.session_state.show_resume_preview = True

    with action2:
        st.download_button(
            "↓  Download Resume",
            data=RESUME_DATA,
            file_name="Akshay_Kumar_Resume.pdf",
            mime="application/pdf",
            disabled=not RESUME_EXISTS,
            use_container_width=True,
            key="hero_resume_download",
        )

    with action3:
        st.markdown(
            """
            <a class="project-view-button" href="#projects">
                ↓&nbsp; View Projects
            </a>
            """,
            unsafe_allow_html=True,
        )

    with action4:
        st.link_button(
            "in",
            "https://www.linkedin.com/in/akshaykumar17/",
            use_container_width=True
        )

    with action5:
        st.link_button(
            "⌘",
            "https://github.com/kumarakshay7",
            use_container_width=True
        )

    with action6:
        st.link_button(
            "✉",
            "mailto:akshaykumar7280@gmail.com",
            use_container_width=True
        )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="location">⌾ &nbsp;Current Location: New Delhi, India</div>',
        unsafe_allow_html=True
    )


# =========================================================
# RIGHT SIDE: IMPACT CARD
# =========================================================

with hero_right:

    st.html("""
    <div class="impact-card">

        <div class="impact-top">
            <div class="impact-label">IMPACT INDEX</div>
            <div class="impact-growth">+62% YoY</div>
        </div>

        <div class="impact-title">Measured outcomes</div>

        <div class="impact-chart">
            <div class="impact-chart-grid"></div>
            <div class="impact-chart-area"></div>
            <div class="impact-chart-line">
                <span class="chart-seg-1"></span>
                <span class="chart-seg-2"></span>
                <span class="chart-seg-3"></span>
                <span class="chart-seg-4"></span>
                <span class="chart-seg-5"></span>
                <span class="chart-seg-6"></span>
                <span class="chart-seg-7"></span>
                <span class="chart-seg-8"></span>
                <span class="chart-seg-9"></span>
                <span class="chart-seg-10"></span>
                <span class="chart-seg-11"></span>
                <span class="chart-seg-12"></span>
            </div>
        </div>

        <div class="impact-metrics">
            <div class="metric-box">
                <div class="metric-number">500K+</div>
                <div class="metric-label">Records processed</div>
            </div>
            <div class="metric-box">
                <div class="metric-number">25%</div>
                <div class="metric-label">Marketing ROI uplift</div>
            </div>
            <div class="metric-box">
                <div class="metric-number">R² 0.85</div>
                <div class="metric-label">MMM model accuracy</div>
            </div>
            <div class="metric-box">
                <div class="metric-number">20+</div>
                <div class="metric-label">Research datasets analyzed</div>
            </div>
        </div>

    </div>
    """)


# =========================================================
# RESUME PREVIEW
# =========================================================

if st.session_state.show_resume_preview and RESUME_EXISTS:

    st.markdown(
        '<div class="resume-preview">',
        unsafe_allow_html=True
    )

    st.subheader("Resume Preview")

    try:

        import pymupdf

        pdf_document = pymupdf.open(
            stream=RESUME_DATA,
            filetype="pdf"
        )

        if pdf_document.page_count == 0:

            st.error("The resume PDF contains no pages.")

        else:

            for page_number in range(pdf_document.page_count):

                page = pdf_document.load_page(page_number)

                pix = page.get_pixmap(
                    matrix=pymupdf.Matrix(1.5, 1.5),
                    alpha=False
                )

                st.image(
                    pix.tobytes("png"),
                    caption=(
                        f"Resume • Page {page_number + 1} "
                        f"of {pdf_document.page_count}"
                    ),
                    use_container_width=True,
                )

        pdf_document.close()

    except ImportError:

        st.error(
            "Resume preview requires PyMuPDF. "
            "Install it with: pip install pymupdf"
        )

    except Exception as exc:

        st.error(
            f"Could not preview the resume PDF: {exc}"
        )

    st.download_button(
        label="↓  Download Resume PDF",
        data=RESUME_DATA,
        file_name="Akshay_Kumar_Resume.pdf",
        mime="application/pdf",
        use_container_width=True,
        key="resume_pdf_download",
    )

    if st.button(
        "✕  Close Resume Preview",
        use_container_width=True,
        key="close_resume_preview"
    ):

        st.session_state.show_resume_preview = False
        st.rerun()

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

# =========================================================
# PROJECTS
# =========================================================

st.markdown(
    '<div id="projects"></div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section">

    <div class="section-label">
    SELECTED WORK
    </div>

    <div class="section-title">
    Projects with measurable impact
    </div>

    <div class="section-description">
    Selected analytics, machine learning and Generative AI
    projects demonstrating practical problem solving and
    technical implementation.
    </div>

    </div>
    """,
    unsafe_allow_html=True
)


project1, project2 = st.columns(2, gap="large")


# =========================================================
# PROJECT CARDS
# Three-column layout matching the reference design
# =========================================================

projects = [
    {
        "key": "mmm",
        "number": "PROJECT 01",
        "category": "MARKETING ANALYTICS",
        "title": "Marketing Mix Modeling",
        "tech": "Python · OLS Regression · Marketing Analytics",
        "description": (
            "Developed an end-to-end Marketing Mix Modeling solution using "
            "OLS regression across 500K+ ad-spend records and 5 marketing "
            "channels. Applied feature engineering, VIF checks, residual "
            "diagnostics and channel contribution analysis to support "
            "marketing budget allocation and ROI optimization."
        ),
        "tags": ["Python", "OLS Regression", "Pandas", "Feature Engineering", "VIF"],
        "metrics": [
            ("0.85", "Model R²"),
            ("+25%", "Budget Efficiency"),
            ("+12%", "Campaign ROI"),
        ],
    },
    {
        "key": "vehicle",
        "number": "PROJECT 02",
        "category": "COMPUTER VISION",
        "title": "Vehicle Detection & Tracking",
        "tech": "Python · YOLOv8 · OpenCV · Deep Learning",
        "description": (
            "Built a computer vision system using YOLOv8 to detect and "
            "classify vehicles from images and video frames. Applied "
            "preprocessing, augmentation and model fine-tuning to improve "
            "detection performance across multiple vehicle classes."
        ),
        "tags": ["Python", "YOLOv8", "OpenCV", "Deep Learning"],
        "metrics": [
            ("10K+", "Images"),
            ("92.4%", "Model mAP"),
            ("30+", "FPS Inference"),
        ],
    },
    {
        "key": "rag",
        "number": "PROJECT 03",
        "category": "GENERATIVE AI · RAG",
        "title": "Enterprise RAG AI Assistant",
        "tech": "LangChain · Azure OpenAI · Azure AI Search · GPT-4o · Streamlit",
        "description": (
            "Developed an end-to-end RAG application for enterprise "
            "document question answering. Implemented document ingestion, "
            "chunking, embeddings, semantic/vector retrieval and grounded "
            "responses using Azure OpenAI and Azure AI Search."
        ),
        "tags": ["LangChain", "Azure OpenAI", "Azure AI Search", "GPT-4o", "Streamlit"],
        "metrics": [
            ("92%", "Grounded Accuracy"),
            ("5K+", "Documents Indexed"),
            ("2.3s", "Avg Response Time"),
        ],
    },
]

for project in projects:
    image_uri = PROJECT_IMAGES.get(project["key"], "")

    if image_uri:
        image_html = (
            '<img src="' + image_uri + '" alt="' +
            project["title"] + ' project visualization">'
        )
    else:
        image_html = (
            '<div class="project-image-placeholder">Image unavailable: ' +
            project["key"] + '.png</div>'
        )

    tags_html = "".join(
        '<span class="project-tag">' + tag + '</span>'
        for tag in project["tags"]
    )

    metrics_html = "".join(
        '<div class="project-metric">'
        '<div class="project-metric-value">' + value + '</div>'
        '<div class="project-metric-label">' + label + '</div>'
        '</div>'
        for value, label in project["metrics"]
    )

    card_html = f"""
    <div class="project-card">
        <div class="project-image-wrap">
            {image_html}
            <div class="project-image-overlay">{project["category"]}</div>
        </div>

        <div class="project-card-body">
            <div class="project-card-top">
                <div class="project-index">{project["number"]}</div>
            </div>

            <div class="project-title">{project["title"]}</div>

            <div class="project-tech">
                {project["tech"]}
            </div>

            <div class="project-card-description">
                {project["description"]}
            </div>

            <div class="project-tags">
                {tags_html}
            </div>

            <div class="project-metric-grid">
                {metrics_html}
            </div>

            <div class="project-repo">
                <a href="{PROJECT_REPOS[project["key"]]}"
                   target="_blank"
                   rel="noopener noreferrer">
                    <span style="font-size:18px;">●</span>
                    &nbsp; View on GitHub
                    <span style="margin-left:8px;">↗</span>
                </a>
            </div>
        </div>
    </div>
    """

    st.html(card_html)



# =========================================================
# EXPERIENCE
# =========================================================

st.markdown(
    '<div id="experience"></div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section">

    <div class="section-label">
    CAREER
    </div>

    <div class="section-title">
    Experience & Education
    </div>

    </div>
    """,
    unsafe_allow_html=True
)


# Protics

st.markdown(
    """
    <div class="experience-card">

    <div class="experience-date">
    September 2025 – Present
    </div>

    <div class="experience-location">
    📍 Sarita Vihar, New Delhi
    </div>

    <div class="experience-title">
    Data Analyst
    </div>

    <div class="experience-company">
    Protics Research
    </div>

    <div class="experience-text">

    ▸ Analyzed market research datasets using SQL and
        Python, improving insight accuracy by 20%.

    <br>

    ▸ Designed and executed quantitative research analysis on 20+ datasets, automating data cleaning and statistical
        evaluation to deliver high-quality insights across 5 industry domains.

    <br>

    ▸  Prepared data processing and reporting workflows using Python, reducing manual effort by 40% and increasing efficiency.

    <br>

    ▸ Applied advanced statistical techniques (correlation, regression, hypothesis testing) across 15+ client studies, identifying
        key drivers that boosted client retention strategies by 12%.

    <br>

    <span class="tag">SQL</span>
    <span class="tag">Python</span>
    <span class="tag">Statistics</span>
    <span class="tag">20+ Datasets</span>

    </div>
    """,
    unsafe_allow_html=True
)


# Course 5

st.markdown(
    """
    <div class="experience-card">

    <div class="experience-date">
    August 2024 – September 2025
    </div>

    <div class="experience-location">
    📍 Coimbatore, Tamil Nadu
    </div>

    <div class="experience-title">
    Analyst
    </div>

    <div class="experience-company">
    Course 5 Intelligence Ltd
    </div>

    <div class="experience-text">

    ▸ Engineered and processed large datasets (500K+ records) in Excel and trained OLS regression models in Python for
       predictive analytics,improving model accuracy by 18% through advanced feature engineering and validation techniques

    <br>

    ▸ Organised and implemented a real-time Marketing Mix Attribution model for 2 CPG clients/brands, achieving a 25%
        uplift in marketing ROI measurement; presented actionable insights to stakeholders to drive strategic decision-making.

    <br>

    ▸ Designed and delivered Power Apps solutions that Analyzed workflow efficiency by 35% and supported faster
        decision-making, contributing to an 8% rise in operational revenue.
    <br>

    ▸ Delivered Power Apps solutions that improved workflow efficiency by 35%.

    </div>

    <br>

    <span class="tag">500K+ Records</span>
    <span class="tag">OLS Regression</span>
    <span class="tag">Marketing Analytics</span>
    <span class="tag">Power Apps</span>

    </div>
    """,
    unsafe_allow_html=True
)


# Education

st.markdown(
    """
    <div class="experience-card">

    <div class="experience-date">
    2022 – 2024
    </div>

    <div class="experience-location">
    📍 Jalandhar, Punjab
    </div>

    <div class="experience-title">
    MBA, Business Analytics
    </div>

    <div class="experience-company">
    Lovely Professional University
    </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SKILLS
# =========================================================

st.markdown(
    '<div id="skills"></div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section">

    <div class="section-label">
    TOOLBOX
    </div>

    <div class="section-title">
    Skills Matrix
    </div>

    </div>
    """,
    unsafe_allow_html=True
)


skill1, skill2 = st.columns(2, gap="large")


with skill1:

    st.markdown(
        """
        <div class="skill-card">

        <div class="skill-title">
        ML & AI
        </div>

        <span class="tag">Regression</span>
        <span class="tag">Classification</span>
        <span class="tag">Time-Series Forecasting</span>
        <span class="tag">Marketing Mix Modeling</span>
        <span class="tag">Deep Learning</span>
        <span class="tag">NLP</span>
        <span class="tag">Computer Vision</span>
        <span class="tag">LLMs & RAG</span>
        <span class="tag">Generative AI</span>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="skill-card">

        <div class="skill-title">
        Engineering
        </div>

        <span class="tag">Python</span>
        <span class="tag">Pandas</span>
        <span class="tag">NumPy</span>
        <span class="tag">SciPy</span>
        <span class="tag">PyTorch</span>
        <span class="tag">TensorFlow</span>
        <span class="tag">SQL</span>
        <span class="tag">REST APIs</span>
        <span class="tag">LangChain</span>

        </div>
        """,
        unsafe_allow_html=True
    )


with skill2:

    st.markdown(
        """
        <div class="skill-card">

        <div class="skill-title">
        Analytics & Statistics
        </div>

        <span class="tag">EDA</span>
        <span class="tag">Hypothesis Testing</span>
        <span class="tag">A/B Testing</span>
        <span class="tag">Feature Engineering</span>
        <span class="tag">Correlation</span>
        <span class="tag">Regression</span>
        <span class="tag">Predictive Analytics</span>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="skill-card">

        <div class="skill-title">
        BI, Cloud & Tools
        </div>

        <span class="tag">Power BI</span>
        <span class="tag">Tableau</span>
        <span class="tag">Advanced Excel</span>
        <span class="tag">Azure OpenAI</span>
        <span class="tag">Azure AI Search</span>
        <span class="tag">Power Apps</span>
        <span class="tag">Power Automate</span>
        <span class="tag">SharePoint</span>
        <span class="tag">Copilot Studio</span>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# CERTIFICATIONS
# =========================================================

st.markdown(
    '<div id="certifications"></div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="section">

    <div class="section-label">
    CREDENTIALS
    </div>

    <div class="section-title">
    Certifications
    </div>

    </div>
    """,
    unsafe_allow_html=True
)


c1, c2, c3 = st.columns(3, gap="large")


with c1:

    st.markdown(
        """
        <div class="cert-card">

        <div style="font-size:30px;">
        🏆
        </div>

        <br>

        <div class="cert-title">
        PL-900: Microsoft Power Platform Fundamentals
        </div>

        <div class="cert-provider">
        ✓ Microsoft
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with c2:

    st.markdown(
        """
        <div class="cert-card">

        <div style="font-size:30px;">
        🤖
        </div>

        <br>

        <div class="cert-title">
        Complete Generative AI Course
        </div>

        <div class="cert-provider">
        ✓ Udemy
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with c3:

    st.markdown(
        """
        <div class="cert-card">

        <div style="font-size:30px;">
        📊
        </div>

        <br>

        <div class="cert-title">
        Analytical Excel Certification Program
        </div>

        <div class="cert-provider">
        ✓ Grant Thornton
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# CONTACT SECTION
# ============================================================

st.markdown("""
<style>

/* CONTACT SECTION */
.contact-title {
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 5px;
    color: #9bb6d5;
    margin-bottom: 25px;
}

.contact-main-title {
    font-size: 48px;
    line-height: 1.08;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 25px;
}

.contact-text {
    font-size: 19px;
    line-height: 1.7;
    color: #9bb6d5;
    margin-bottom: 22px;
}

.contact-text strong {
    color: #ffffff;
}

.contact-tag {
    display: inline-block;
    background: #0d1522;
    border: 1px solid #18365e;
    color: #3d86ff;
    border-radius: 8px;
    padding: 9px 14px;
    margin: 5px 5px 5px 0;
    font-size: 14px;
    font-weight: 700;
}

.connect-title {
    color: #ffffff;
    font-size: 22px;
    font-weight: 750;
    margin-top: 8px;
    margin-bottom: 10px;
}

.connect-text {
    color: #9bb6d5;
    font-size: 18px;
    line-height: 1.55;
    margin-bottom: 3px !important;
}

.contact-info {
    color: #ffffff;
    font-size: 16px;
    font-weight: 600;
    margin: 3px 0 !important;
}

.contact-form-box {
    background: #0d1016;
    border: 1px solid #1b2635;
    border-radius: 10px;
    padding: 25px;
}

/* Streamlit form inputs */
div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea {
    background: #090b0f !important;
    color: #ffffff !important;
    border: 1px solid #1d2a3b !important;
    border-radius: 8px !important;
    padding: 15px !important;
    font-size: 16px !important;
}

div[data-testid="stTextInput"] input:focus,
div[data-testid="stTextArea"] textarea:focus {
    border-color: #3d86ff !important;
    box-shadow: none !important;
}

div[data-testid="stTextInput"] input::placeholder,
div[data-testid="stTextArea"] textarea::placeholder {
    color: #566b84 !important;
}

/* Hide Streamlit labels */
.contact-form-box label {
    color: #9bb6d5 !important;
}

/* Send button */
div.stButton > button {
    background: #3d86ff !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 14px 28px !important;
    font-size: 17px !important;
    font-weight: 700 !important;
}

div.stButton > button:hover {
    background: #3478e5 !important;
    color: #ffffff !important;
}

/* Mobile */
@media (max-width: 900px) {

    .contact-main-title {
        font-size: 40px;
    }

    .contact-text {
        font-size: 17px;
    }

    .contact-form-box {
        padding: 25px;
        margin-top: 30px;
    }

}

</style>
""", unsafe_allow_html=True)


# ------------------------------------------------------------
# SECTION LABEL
# ------------------------------------------------------------

st.markdown(
    '<div class="contact-title">GET IN TOUCH</div>',
    unsafe_allow_html=True
)


# ------------------------------------------------------------
# TWO COLUMNS
# ------------------------------------------------------------

contact_left, contact_right = st.columns(
    [0.9, 1.1],
    gap="large"
)


# ============================================================
# LEFT SIDE
# ============================================================

with contact_left:

    st.markdown(
        """
        <div class="contact-main-title">
            Looking for my next<br>
            opportunity
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="contact-text">
            I'm currently open to
            <strong>Data Analyst,</strong>
            <strong>Data Scientist, and AI/ML opportunities</strong>
            where I can use data, analytics, and AI to solve
            real-world business problems.
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="contact-text">
            If you're a recruiter,or someone
            working on an interesting analytics project, I'd be
            happy to connect and discuss potential opportunities.
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <span class="contact-tag">Analytics Roles</span>
        <span class="contact-tag">AI/ML Roles</span>
        <span class="contact-tag">Data Science Roles</span>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="connect-title">Let\'s Connect</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="connect-text">
            Have an opportunity that matches my profile?
            Feel free to reach out. I'd be happy to discuss
            how I can contribute to your team.
        </div>
        """,
        unsafe_allow_html=True
    )
st.html("""
<div style="margin-top:5px;">

    <!-- Email -->
    <div class="contact-info" style="margin:5px 0;">
        ✉ &nbsp;&nbsp; akshaykumar7280@gmail.com
    </div>

    <!-- Phone + Social Links -->
    <div style="
        display:flex;
        align-items:center;
        gap:8px;
        margin-top:5px;
        flex-wrap:wrap;
    ">

        <!-- Phone -->
        <div class="contact-info" style="margin:0;">
            ☎ &nbsp;&nbsp; +91 77620 40867
        </div>

        <!-- LinkedIn -->
        <a href="https://www.linkedin.com/in/akshaykumar17/"
           target="_blank"
           style="
           display:inline-flex;
           align-items:center;
           justify-content:center;
           width:42px;
           height:42px;
           border:1px solid #1d2a3b;
           border-radius:9px;
           color:#ffffff;
           background:#090c11;
           text-decoration:none;
           font-weight:700;">
           in
        </a>

        <!-- GitHub -->
        <a href="https://github.com/"
           target="_blank"
           style="
           display:inline-flex;
           align-items:center;
           justify-content:center;
           width:42px;
           height:42px;
           border:1px solid #1d2a3b;
           border-radius:9px;
           color:#ffffff;
           background:#090c11;
           text-decoration:none;
           font-weight:700;">
           Git
        </a>

    </div>

</div>
""")

# ============================================================
# RIGHT SIDE
# ============================================================

with contact_right:

    # Show success message above the form
    if st.session_state.get("message_sent", False):

        st.success(
            "✅ Message sent successfully! I'll get back to you soon."
        )

        st.session_state.message_sent = False


    # Real Streamlit container
    with st.container(border=True):

        st.markdown(
            '<div class="contact-title" style="letter-spacing:0px;">NAME</div>',
            unsafe_allow_html=True
        )

        name = st.text_input(
            "Your name",
            placeholder="Your name",
            label_visibility="collapsed",
            key="portfolio_name"
        )


        st.markdown(
            '<div class="contact-title" style="letter-spacing:4px; margin-top:10px;">EMAIL</div>',
            unsafe_allow_html=True
        )

        email = st.text_input(
            "Your email",
            placeholder="you@company.com",
            label_visibility="collapsed",
            key="portfolio_email"
        )


        st.markdown(
            '<div class="contact-title" style="letter-spacing:4px; margin-top:20px;">MESSAGE</div>',
            unsafe_allow_html=True
        )

        message = st.text_area(
            "Your message",
            placeholder="Tell me about the role or project...",
            height=160,
            label_visibility="collapsed",
            key="portfolio_message"
        )


        send_message = st.button(
            "➤  Send Message",
            key="portfolio_send"
        )


# ============================================================
# ============================================================
# SEND EMAIL
# ============================================================

if send_message:

    if not name or not email or not message:

        st.warning(
            "Please fill in your name, email and message."
        )

    else:

        import smtplib
        from email.message import EmailMessage

        try:

            sender_email = st.secrets["EMAIL_ADDRESS"]
            sender_password = st.secrets["EMAIL_APP_PASSWORD"]

            receiver_email = "akshaykumar7280@gmail.com"

            msg = EmailMessage()

            msg["Subject"] = f"Portfolio Contact - {name}"
            msg["From"] = sender_email
            msg["To"] = receiver_email
            msg["Reply-To"] = email

            msg.set_content(
                f"""
New message from your Portfolio Website

Name:
{name}

Email:
{email}

Message:
{message}
"""
            )

            with smtplib.SMTP_SSL(
                "smtp.gmail.com",
                465
            ) as smtp:

                smtp.login(
                    sender_email,
                    sender_password
                )

                smtp.send_message(msg)

            # Tell the page to show success message
            st.session_state.message_sent = True

            # Rerun so success appears at the top of the form
            st.rerun()

        except Exception as e:

            st.error(
                f"❌ Could not send the message: {e}"
            )
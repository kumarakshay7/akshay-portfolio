import base64
import smtplib
from email.message import EmailMessage
from pathlib import Path

import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
ASSET_DIR = BASE_DIR / "assets" / "images"
RESUME_PATH = BASE_DIR / "resume.pdf"

st.set_page_config(
    page_title="Akshay Kumar | Data Analyst & AI/ML",
    page_icon="AK",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------
def image_data_uri(path: Path) -> str:
    if not path.exists() or path.stat().st_size == 0:
        return ""
    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:image/png;base64,{encoded}"


PROJECT_IMAGES = {
    "mmm": image_data_uri(ASSET_DIR / "mmm.png"),
    "vehicle": image_data_uri(ASSET_DIR / "vehicle.png"),
    "rag": image_data_uri(ASSET_DIR / "rag.png"),
}

RESUME_EXISTS = RESUME_PATH.exists() and RESUME_PATH.stat().st_size > 0
RESUME_DATA = RESUME_PATH.read_bytes() if RESUME_EXISTS else b""

GITHUB = "https://github.com/kumarakshay7"
LINKEDIN = "https://www.linkedin.com/in/akshaykumar17/"
EMAIL = "akshaykumar7280@gmail.com"
PHONE = "+91 77620 40867"

PROJECTS = [
    {
        "number": "01",
        "category": "MARKETING ANALYTICS",
        "title": "Marketing Mix Modeling",
        "subtitle": "Budget allocation & ROI measurement",
        "image": "mmm",
        "description": (
            "Built an end-to-end Marketing Mix Modeling workflow using OLS "
            "regression, feature engineering, VIF checks, validation and "
            "channel contribution analysis across 500K+ records and 5 marketing channels."
        ),
        "stack": ["Python", "OLS Regression", "Pandas", "VIF", "Time Series"],
        "metrics": [("500K+", "records"), ("R² 0.85", "model fit"), ("+25%", "budget efficiency"), ("+12%", "ROI")],
        "link": None,
        "link_label": "Professional case study",
    },
    {
        "number": "02",
        "category": "GENERATIVE AI · RAG",
        "title": "Enterprise RAG AI Assistant",
        "subtitle": "Grounded document question answering",
        "image": "rag",
        "description": (
            "Implemented an enterprise RAG pipeline with document ingestion, "
            "chunking, embeddings, semantic/vector retrieval and grounded response generation "
            "using Azure OpenAI, Azure AI Search, LangChain and Streamlit."
        ),
        "stack": ["Azure OpenAI", "Azure AI Search", "LangChain", "Embeddings", "Streamlit"],
        "metrics": [("E2E", "RAG pipeline"), ("Vector", "retrieval"), ("Semantic", "search"), ("Grounded", "responses")],
        "link": "https://github.com/kumarakshay7/Azure-RAG-Assignments",
        "link_label": "View GitHub repository",
    },
    {
        "number": "03",
        "category": "COMPUTER VISION",
        "title": "Vehicle Detection & Tracking",
        "subtitle": "YOLOv8-based video analytics",
        "image": "vehicle",
        "description": (
            "Built a computer vision workflow for vehicle detection and tracking using YOLOv8 "
            "and OpenCV, including image/video preprocessing, model training and inference."
        ),
        "stack": ["Python", "YOLOv8", "OpenCV", "Deep Learning"],
        "metrics": [("YOLOv8", "detector"), ("Video", "inference"), ("OpenCV", "vision"), ("C5i", "project")],
        "link": None,
        "link_label": "Professional case study",
    },
    {
        "number": "04",
        "category": "ML ENGINEERING",
        "title": "YOLO11 Model Optimization",
        "subtitle": "Training, ONNX export & INT8 evaluation",
        "image": None,
        "description": (
            "Completed an object-detection engineering workflow covering model training, "
            "evaluation, ONNX export, FP32 validation, INT8 quantization and failure analysis."
        ),
        "stack": ["YOLO11", "PyTorch", "ONNX", "INT8", "Python"],
        "metrics": [("YOLO11", "model"), ("ONNX", "deployment"), ("INT8", "quantization"), ("ML", "evaluation")],
        "link": "https://github.com/kumarakshay7/artikate-cv-ml-engineer-assignment",
        "link_label": "View GitHub repository",
    },
    {
        "number": "05",
        "category": "POWER PLATFORM · BI",
        "title": "Power Platform & BI Automation",
        "subtitle": "Workflow automation & decision support",
        "image": None,
        "description": (
            "Designed Power Apps and Power Automate solutions with SharePoint integration, "
            "Copilot Studio and BI reporting to streamline operational workflows and support faster decisions."
        ),
        "stack": ["Power Apps", "Power Automate", "SharePoint", "Copilot Studio", "Power BI"],
        "metrics": [("35%", "workflow efficiency"), ("8%", "operational revenue"), ("Power Apps", "solutions"), ("BI", "reporting")],
        "link": None,
        "link_label": "Professional case study",
    },
]


# -------------------------------------------------------------------
# CSS
# -------------------------------------------------------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

:root {
    --bg: #07090d;
    --panel: #0d1118;
    --panel-2: #101722;
    --line: #1c2736;
    --line-soft: rgba(255,255,255,.07);
    --text: #f5f7fb;
    --muted: #8fa0b5;
    --blue: #4b8dff;
    --cyan: #35d5ff;
    --green: #58d68d;
}

html { scroll-behavior: smooth; }

.stApp {
    background:
      radial-gradient(circle at 15% 8%, rgba(75,141,255,.10), transparent 28%),
      radial-gradient(circle at 85% 20%, rgba(53,213,255,.06), transparent 24%),
      linear-gradient(rgba(255,255,255,.018) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255,255,255,.018) 1px, transparent 1px),
      var(--bg);
    background-size: auto, auto, 72px 72px, 72px 72px;
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
}

.block-container { max-width: 1240px; padding: 0 2rem 3rem; }
#MainMenu, footer, header { visibility: hidden; }

a { transition: .2s ease; }

/* NAV */
.nav {
    position: sticky;
    top: 0;
    z-index: 20;
    min-height: 68px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid var(--line-soft);
    background: rgba(7,9,13,.82);
    backdrop-filter: blur(16px);
}
.nav-brand {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 23px;
    font-weight: 700;
    color: #fff;
}
.nav-brand span { color: var(--blue); }
.nav-links { display:flex; gap: 28px; align-items:center; }
.nav-links a { color:#9aa9bc; text-decoration:none; font-size:14px; }
.nav-links a:hover { color:#fff; }
.nav-cta {
    color:#fff !important;
    border:1px solid #29456f;
    background:#0e1827;
    border-radius:8px;
    padding:9px 14px;
}
@media(max-width:850px) {
    .nav-links a:not(.nav-cta) { display:none; }
}

/* HERO */
.hero { padding: 105px 0 85px; }
.kicker {
    display:inline-flex;
    align-items:center;
    gap:9px;
    color:#a9bad0;
    font-size:12px;
    letter-spacing:2.5px;
    text-transform:uppercase;
    font-weight:700;
}
.kicker-dot {
    width:7px; height:7px; border-radius:50%;
    background:var(--green);
    box-shadow:0 0 16px rgba(88,214,141,.8);
}
.hero h1 {
    font-family:'Space Grotesk', sans-serif;
    font-size:clamp(54px,8vw,94px);
    line-height:.96;
    letter-spacing:-4px;
    margin:22px 0 16px;
    color:#fff;
}
.hero h1 span { color:var(--blue); }
.hero h2 {
    font-family:'Space Grotesk', sans-serif;
    font-size:clamp(25px,3.2vw,40px);
    line-height:1.15;
    letter-spacing:-1.4px;
    color:#93a6bf;
    margin:0;
}
.hero-copy {
    max-width:720px;
    margin-top:26px;
    color:#91a1b5;
    font-size:17px;
    line-height:1.8;
}
.hero-actions { margin-top:30px; display:flex; gap:10px; flex-wrap:wrap; }
.hero-actions a {
    display:inline-flex; align-items:center; justify-content:center;
    min-height:46px; padding:0 18px; border-radius:8px;
    text-decoration:none; font-weight:700; font-size:14px;
}
.btn-primary { background:var(--blue); color:#fff !important; }
.btn-secondary { border:1px solid #26364d; background:#0d141e; color:#dce6f2 !important; }
.btn-secondary:hover { border-color:#4b8dff; }
.hero-note { color:#687b93; font-size:13px; margin-top:17px; }

/* HERO STATS */
.stat-panel {
    height:100%;
    min-height:390px;
    padding:27px;
    border:1px solid var(--line);
    border-radius:16px;
    background:linear-gradient(145deg, rgba(16,23,34,.98), rgba(9,13,19,.98));
    box-shadow:0 25px 80px rgba(0,0,0,.25);
}
.stat-head { display:flex; justify-content:space-between; align-items:center; }
.stat-label { color:#8499b2; font-size:11px; letter-spacing:2px; font-weight:700; }
.stat-live { color:var(--green); font-size:11px; font-weight:700; }
.stat-title {
    font-family:'Space Grotesk',sans-serif; font-size:29px; font-weight:700;
    margin:13px 0 25px;
}
.big-stat {
    border-top:1px solid var(--line);
    padding:20px 0;
    display:flex; justify-content:space-between; gap:20px;
}
.big-number { color:#fff; font-family:'Space Grotesk',sans-serif; font-size:32px; font-weight:700; }
.big-label { color:#7e91aa; font-size:13px; margin-top:5px; text-align:right; }
.stat-foot {
    margin-top:12px; padding:13px 14px; border-radius:9px;
    background:#0a111a; border:1px solid #172334; color:#8ea2bb; font-size:13px;
}

/* SECTION */
.section { padding-top:85px; scroll-margin-top:85px; }
.section-kicker { color:#6f88a5; font-size:11px; letter-spacing:3px; font-weight:700; }
.section-title {
    font-family:'Space Grotesk',sans-serif; color:#fff;
    font-size:clamp(34px,4vw,52px); line-height:1.05;
    letter-spacing:-2px; margin:11px 0 13px;
}
.section-copy { max-width:780px; color:#8496ad; font-size:16px; line-height:1.75; }

/* PROJECTS */
.project-card {
    overflow:hidden; height:100%; min-height:610px;
    border:1px solid var(--line); border-radius:15px;
    background:linear-gradient(180deg,#0d131c,#090d13);
    transition:transform .25s ease,border-color .25s ease,box-shadow .25s ease;
    margin-bottom:24px;
}
.project-card:hover {
    transform:translateY(-5px); border-color:#2f5f9e;
    box-shadow:0 25px 65px rgba(0,0,0,.25);
}
.project-visual {
    height:245px; padding:10px; position:relative; overflow:hidden;
    display:flex; align-items:center; justify-content:center;
    background:radial-gradient(circle at 50% 20%,rgba(75,141,255,.13),transparent 55%),#080c12;
    border-bottom:1px solid var(--line);
}
.project-visual img { width:100%; height:100%; object-fit:contain; border-radius:9px; }
.visual-placeholder {
    width:92%; height:82%; border:1px solid #21334a; border-radius:12px;
    background:
      linear-gradient(135deg,rgba(75,141,255,.13),transparent 55%),
      #0b1119;
    display:flex; align-items:center; justify-content:center;
    position:relative; overflow:hidden;
}
.visual-placeholder:before {
    content:""; position:absolute; inset:20px;
    border:1px dashed #29415f; border-radius:9px;
}
.visual-code {
    color:#7fa9dc; font-family:monospace; font-size:12px; line-height:1.8;
    z-index:1; text-align:left;
}
.category {
    position:absolute; left:20px; bottom:17px;
    background:rgba(6,10,16,.82); border:1px solid rgba(255,255,255,.13);
    border-radius:6px; padding:6px 9px; color:#b6c8dc;
    font-size:10px; letter-spacing:1.4px; font-weight:700;
    backdrop-filter:blur(8px);
}
.project-body { padding:25px 25px 27px; }
.project-number { color:#4b8dff; font-size:11px; letter-spacing:2px; font-weight:800; }
.project-title { color:#fff; font-family:'Space Grotesk',sans-serif; font-size:26px; font-weight:700; margin-top:8px; }
.project-subtitle { color:#7e93ad; font-size:13px; margin-top:4px; }
.project-desc { color:#899bb0; font-size:14px; line-height:1.72; margin-top:16px; }
.tags { display:flex; flex-wrap:wrap; gap:7px; margin-top:16px; }
.tag { border:1px solid #203149; background:#0d1621; color:#9db2cb; border-radius:6px; padding:5px 8px; font-size:11px; }
.metrics { display:grid; grid-template-columns:repeat(4,1fr); gap:7px; margin-top:20px; }
.metric { padding:10px 8px; border:1px solid #19283b; background:#0a1018; border-radius:7px; }
.metric strong { display:block; color:#e9f0f8; font-size:14px; }
.metric span { display:block; color:#667d98; font-size:9px; margin-top:3px; }
.project-link { display:inline-flex; margin-top:20px; color:#a9c8f2; text-decoration:none; font-size:12px; font-weight:700; }
.project-link:hover { color:#fff; }
@media(max-width:700px) { .metrics { grid-template-columns:repeat(2,1fr); } .project-card { min-height:auto; } }

/* EXPERIENCE */
.timeline { border-left:1px solid #233249; margin-top:28px; padding-left:28px; }
.timeline-item { position:relative; padding:0 0 38px; }
.timeline-item:before {
    content:""; position:absolute; width:9px; height:9px; border-radius:50%;
    background:var(--blue); left:-33px; top:7px; box-shadow:0 0 0 5px #0a111a;
}
.timeline-date { color:#5f83b2; font-size:12px; letter-spacing:1.3px; font-weight:700; }
.timeline-role { color:#fff; font-family:'Space Grotesk',sans-serif; font-size:25px; font-weight:700; margin-top:7px; }
.timeline-company { color:#a0b0c3; font-size:15px; margin-top:3px; }
.timeline-text { color:#8294aa; font-size:14px; line-height:1.8; margin-top:12px; }
.timeline-tags { margin-top:13px; display:flex; flex-wrap:wrap; gap:7px; }

/* SKILLS */
.skill-card {
    border:1px solid var(--line); border-radius:13px; padding:23px;
    background:#0b1017; height:100%; margin-bottom:16px;
}
.skill-card h3 { color:#fff; font-family:'Space Grotesk',sans-serif; font-size:19px; margin:0 0 14px; }
.skill-list { color:#8fa2b9; line-height:2; font-size:14px; }

/* CONTACT */
.contact-shell {
    margin-top:30px; padding:30px; border:1px solid var(--line); border-radius:15px;
    background:linear-gradient(145deg,#0d141e,#090d13);
}
.contact-title { color:#fff; font-family:'Space Grotesk',sans-serif; font-size:42px; line-height:1.1; letter-spacing:-1.5px; }
.contact-copy { color:#899bb0; line-height:1.8; margin-top:15px; }
.contact-links { margin-top:22px; }
.contact-links a { color:#9fc1ec; text-decoration:none; margin-right:18px; font-size:13px; }
.contact-links a:hover { color:#fff; }
div[data-testid="stTextInput"] input, div[data-testid="stTextArea"] textarea {
    background:#080c12 !important; color:#fff !important;
    border:1px solid #203047 !important; border-radius:8px !important;
}
div[data-testid="stTextInput"] input:focus, div[data-testid="stTextArea"] textarea:focus {
    border-color:#4b8dff !important; box-shadow:none !important;
}
div.stButton > button {
    background:#4b8dff !important; color:#fff !important; border:0 !important;
    border-radius:8px !important; font-weight:700 !important;
}
.footer {
    margin-top:80px; padding:28px 0 10px; border-top:1px solid var(--line-soft);
    color:#60728a; font-size:12px; text-align:center;
}
</style>
""",
    unsafe_allow_html=True,
)

# -------------------------------------------------------------------
# Navigation
# -------------------------------------------------------------------
st.markdown(
    f"""
<div class="nav">
  <div class="nav-brand">AK<span>.</span></div>
  <div class="nav-links">
    <a href="#work">Work</a>
    <a href="#experience">Experience</a>
    <a href="#skills">Skills</a>
    <a href="#contact" class="nav-cta">Let's connect ↗</a>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# -------------------------------------------------------------------
# Hero
# -------------------------------------------------------------------
st.markdown('<div class="hero">', unsafe_allow_html=True)
hero_left, hero_right = st.columns([1.45, .75], gap="large")

with hero_left:
    st.markdown(
        """
<div class="kicker"><span class="kicker-dot"></span> Data Analyst · Machine Learning · GenAI</div>
<h1>Akshay <span>Kumar</span></h1>
<h2>Turning data into decisions and models into useful products.</h2>
<div class="hero-copy">
I work across analytics, machine learning, Generative AI and automation.
My projects span Marketing Mix Modeling, enterprise RAG, computer vision,
model optimization and Power Platform solutions.
</div>
<div class="hero-actions">
  <a class="btn-primary" href="#work">Explore my work ↓</a>
  <a class="btn-secondary" href="https://github.com/kumarakshay7" target="_blank">GitHub ↗</a>
  <a class="btn-secondary" href="https://www.linkedin.com/in/akshaykumar17/" target="_blank">LinkedIn ↗</a>
</div>
<div class="hero-note">Open to Data Analyst, Data Scientist and AI/ML opportunities.</div>
""",
        unsafe_allow_html=True,
    )

with hero_right:
    st.markdown(
        """
<div class="stat-panel">
  <div class="stat-head">
    <div class="stat-label">SELECTED IMPACT</div>
    <div class="stat-live">● ACTIVE</div>
  </div>
  <div class="stat-title">Built around measurable outcomes.</div>

  <div class="big-stat">
    <div><div class="big-number">500K+</div><div class="stat-foot">records handled in analytics workflows</div></div>
    <div class="big-label">DATA SCALE</div>
  </div>
  <div class="big-stat">
    <div><div class="big-number">+25%</div><div class="stat-foot">budget efficiency in MMM work</div></div>
    <div class="big-label">MMM</div>
  </div>
  <div class="big-stat">
    <div><div class="big-number">+35%</div><div class="stat-foot">workflow efficiency through Power Apps solutions</div></div>
    <div class="big-label">AUTOMATION</div>
  </div>
  <div class="stat-foot">Python · SQL · Azure · Power Platform · ML · GenAI</div>
</div>
""",
        unsafe_allow_html=True,
    )

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------------------------
# Resume actions
# -------------------------------------------------------------------
if RESUME_EXISTS:
    c1, c2, c3 = st.columns([1, 1, 3])
    with c1:
        st.download_button(
            "↓ Download Resume",
            data=RESUME_DATA,
            file_name="Akshay_Kumar_Resume.pdf",
            mime="application/pdf",
            use_container_width=True,
        )
    with c2:
        if st.button("View Resume", use_container_width=True):
            st.session_state["show_resume"] = not st.session_state.get("show_resume", False)

if st.session_state.get("show_resume") and RESUME_EXISTS:
    st.markdown('<div class="contact-shell">', unsafe_allow_html=True)
    st.subheader("Resume preview")
    try:
        import pymupdf
        doc = pymupdf.open(stream=RESUME_DATA, filetype="pdf")
        for i in range(doc.page_count):
            pix = doc.load_page(i).get_pixmap(matrix=pymupdf.Matrix(1.25, 1.25), alpha=False)
            st.image(pix.tobytes("png"), caption=f"Page {i + 1}", use_container_width=True)
        doc.close()
    except Exception as exc:
        st.error(f"Could not preview the resume: {exc}")
    st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------------------------
# Projects
# -------------------------------------------------------------------
st.markdown('<div id="work" class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-kicker">SELECTED WORK</div><div class="section-title">Projects that show how I work.</div><div class="section-copy">A mix of professional case studies and public engineering projects, covering analytics, machine learning, Generative AI and automation.</div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

for row_start in range(0, len(PROJECTS), 2):
    cols = st.columns(2, gap="large")
    for idx, project in enumerate(PROJECTS[row_start:row_start + 2]):
        with cols[idx]:
            image_uri = PROJECT_IMAGES.get(project["image"], "") if project["image"] else ""
            if image_uri:
                visual = f'<img src="{image_uri}" alt="{project["title"]} project visualization">'
            else:
                code_lines = {
                    "04": "model → export → quantize\nFP32 → ONNX → INT8\nevaluate → analyze → verify",
                    "05": "Power Apps\n   ↓\nPower Automate → SharePoint\n   ↓\nBI / Copilot Studio",
                }.get(project["number"], "analytics → model → insight")
                visual = f'<div class="visual-placeholder"><div class="visual-code">{code_lines.replace(chr(10), "<br>")}</div></div>'

            tags = "".join(f'<span class="tag">{tag}</span>' for tag in project["stack"])
            metrics = "".join(
                f'<div class="metric"><strong>{value}</strong><span>{label}</span></div>'
                for value, label in project["metrics"]
            )
            link_html = (
                f'<a class="project-link" href="{project["link"]}" target="_blank">↗ {project["link_label"]}</a>'
                if project["link"]
                else f'<div class="project-link" style="color:#667d98;">◆ {project["link_label"]}</div>'
            )

            st.markdown(
                f"""
<div class="project-card">
  <div class="project-visual">{visual}<div class="category">{project["category"]}</div></div>
  <div class="project-body">
    <div class="project-number">PROJECT {project["number"]}</div>
    <div class="project-title">{project["title"]}</div>
    <div class="project-subtitle">{project["subtitle"]}</div>
    <div class="project-desc">{project["description"]}</div>
    <div class="tags">{tags}</div>
    <div class="metrics">{metrics}</div>
    {link_html}
  </div>
</div>
""",
                unsafe_allow_html=True,
            )

# -------------------------------------------------------------------
# Experience
# -------------------------------------------------------------------
st.markdown('<div id="experience" class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-kicker">CAREER</div><div class="section-title">Experience & education.</div><div class="section-copy">A concise view of recent analytics experience and the business problems behind the work.</div>', unsafe_allow_html=True)
st.markdown(
    """
<div class="timeline">
  <div class="timeline-item">
    <div class="timeline-date">SEPTEMBER 2025 — PRESENT</div>
    <div class="timeline-role">Data Analyst</div>
    <div class="timeline-company">Protics Research</div>
    <div class="timeline-text">
      Worked with market research datasets using SQL and Python; designed quantitative analysis,
      data-cleaning and reporting workflows across multiple studies and industry domains.
      Applied correlation, regression and hypothesis testing to identify useful business drivers.
    </div>
    <div class="timeline-tags"><span class="tag">SQL</span><span class="tag">Python</span><span class="tag">Statistics</span><span class="tag">Market Research</span></div>
  </div>

  <div class="timeline-item">
    <div class="timeline-date">AUGUST 2024 — SEPTEMBER 2025</div>
    <div class="timeline-role">Analyst</div>
    <div class="timeline-company">Course 5 Intelligence Ltd</div>
    <div class="timeline-text">
      Built analytics and automation solutions across Marketing Mix Modeling, predictive analytics,
      computer vision and Power Platform. Processed 500K+ records, built OLS models, supported MMM
      for 2 CPG clients/brands and delivered Power Apps solutions that improved workflow efficiency by 35%.
    </div>
    <div class="timeline-tags"><span class="tag">MMM</span><span class="tag">OLS</span><span class="tag">Power Apps</span><span class="tag">Computer Vision</span></div>
  </div>

  <div class="timeline-item">
    <div class="timeline-date">2022 — 2024</div>
    <div class="timeline-role">MBA, Business Analytics</div>
    <div class="timeline-company">Lovely Professional University</div>
    <div class="timeline-text">Academic focus on business analytics, data-driven decision making and applied analytical methods.</div>
    <div class="timeline-tags"><span class="tag">Business Analytics</span><span class="tag">MBA</span></div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------------------------
# Skills
# -------------------------------------------------------------------
st.markdown('<div id="skills" class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-kicker">TOOLBOX</div><div class="section-title">Technical skills.</div><div class="section-copy">Tools and methods used across analytics, machine learning, Generative AI and business automation.</div>', unsafe_allow_html=True)

skill_data = [
    ("Analytics & Statistics", "SQL · Python · Pandas · NumPy · SciPy · EDA · Regression · Hypothesis Testing · Feature Engineering · Predictive Analytics"),
    ("Machine Learning", "Marketing Mix Modeling · Time Series Forecasting · Classification · Deep Learning · Computer Vision · YOLOv8 · YOLO11 · OpenCV"),
    ("Generative AI", "RAG · LLMs · LangChain · Embeddings · Azure OpenAI · Azure AI Search · Prompt Engineering · Streamlit"),
    ("BI & Automation", "Power BI · Tableau · Advanced Excel · Power Apps · Power Automate · SharePoint · Copilot Studio"),
    ("Engineering", "REST APIs · Java · Spring Boot · MySQL · Git/GitHub · ONNX · PyTorch · TensorFlow"),
    ("Cloud", "Azure · Azure OpenAI · Azure AI Search"),
]
for start in range(0, len(skill_data), 2):
    cols = st.columns(2, gap="large")
    for j, (title, body) in enumerate(skill_data[start:start+2]):
        with cols[j]:
            st.markdown(f'<div class="skill-card"><h3>{title}</h3><div class="skill-list">{body}</div></div>', unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------------------------
# Certifications
# -------------------------------------------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="section-kicker">CREDENTIALS</div><div class="section-title">Certifications.</div>', unsafe_allow_html=True)
certs = [
    ("PL-900", "Microsoft Power Platform Fundamentals", "Microsoft"),
    ("GENAI", "Complete Generative AI Course", "Udemy"),
    ("EXCEL", "Analytical Excel Certification Program", "Grant Thornton"),
]
cols = st.columns(3, gap="large")
for col, (code, title, provider) in zip(cols, certs):
    with col:
        st.markdown(f'<div class="skill-card"><div class="section-kicker">{code}</div><h3>{title}</h3><div class="skill-list">{provider}</div></div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------------------------
# Contact
# -------------------------------------------------------------------
st.markdown('<div id="contact" class="section">', unsafe_allow_html=True)
st.markdown('<div class="contact-shell">', unsafe_allow_html=True)
left, right = st.columns([.9, 1.1], gap="large")

with left:
    st.markdown('<div class="section-kicker">GET IN TOUCH</div><div class="contact-title">Let’s build something useful with data.</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="contact-copy">I’m open to conversations around Data Analyst, Data Scientist and AI/ML opportunities, analytics projects and applied Generative AI work.</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<div class="contact-links"><a href="mailto:{EMAIL}">✉ {EMAIL}</a><a href="tel:{PHONE.replace(" ", "")}">☎ {PHONE}</a><br><br><a href="{LINKEDIN}" target="_blank">LinkedIn ↗</a><a href="{GITHUB}" target="_blank">GitHub ↗</a></div>',
        unsafe_allow_html=True,
    )

with right:
    name = st.text_input("Name", placeholder="Your name", key="contact_name")
    email = st.text_input("Email", placeholder="you@company.com", key="contact_email")
    message = st.text_area("Message", placeholder="Tell me about the role or project...", height=145, key="contact_message")
    if st.button("Send message ↗", key="send_message"):
        if not name or not email or not message:
            st.warning("Please fill in your name, email and message.")
        else:
            try:
                sender = st.secrets["EMAIL_ADDRESS"]
                password = st.secrets["EMAIL_APP_PASSWORD"]
                msg = EmailMessage()
                msg["Subject"] = f"Portfolio Contact - {name}"
                msg["From"] = sender
                msg["To"] = EMAIL
                msg["Reply-To"] = email
                msg.set_content(f"New portfolio message\n\nName: {name}\nEmail: {email}\n\n{message}")
                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                    smtp.login(sender, password)
                    smtp.send_message(msg)
                st.success("Message sent successfully. Thank you!")
            except Exception as exc:
                st.error("The message could not be sent. Please use the email or LinkedIn links instead.")

st.markdown("</div></div>", unsafe_allow_html=True)

# -------------------------------------------------------------------
# Footer
# -------------------------------------------------------------------
st.markdown(
    '<div class="footer">© 2026 Akshay Kumar · Data Analytics · Machine Learning · Generative AI</div>',
    unsafe_allow_html=True,
)

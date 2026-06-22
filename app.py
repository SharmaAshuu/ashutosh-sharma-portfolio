"""
app.py — Streamlit Resume App for Ashutosh Sharma
Run locally : streamlit run app.py
Deploy      : Push to GitHub → connect to Streamlit Cloud
"""

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Ashutosh Sharma | Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Load assets ──────────────────────────────────────────────────────────────
def load_file(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")

html_content = load_file("index.html")
css_content  = load_file("style.css")

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 👤 Ashutosh Sharma")
    st.markdown("**Data Analyst** · Pune, India")
    st.divider()

    st.markdown("### 🔗 Navigate")
    # JavaScript postMessage scrolls to section inside the iframe
    nav_items = [
        ("🏠", "Home",      "home"),
        ("🙋", "About Me",  "about"),
        ("🛠️", "Skills",    "skills"),
        ("📁", "Projects",  "projects"),
        ("🎓", "Education", "education"),
        ("📬", "Contact",   "contact"),
    ]
    for icon, label, anchor in nav_items:
        if st.button(f"{icon} {label}", key=anchor, use_container_width=True):
            # JS injected to scroll the iframe to the anchor
            st.markdown(
                f"<script>document.getElementById('resume-frame')"
                f".contentWindow.document.getElementById('{anchor}')"
                f".scrollIntoView({{behavior:'smooth'}});</script>",
                unsafe_allow_html=True,
            )

    st.divider()
    st.markdown("### 📬 Quick Contact")
    st.markdown("📧 sharma.ashutosh.work@gmail.com")
    st.markdown("📞 +91 92840 73347")

    st.divider()
    st.markdown("### 🌐 Links")
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("LinkedIn", "https://linkedin.com/in/ashutosh-sharma-in",
                       use_container_width=True)
    with col2:
        st.link_button("GitHub", "https://github.com/SharmaAshuu",
                       use_container_width=True)

    st.divider()
    st.caption("© Ashutosh Sharma · Built with Streamlit")

# ── Hide Streamlit chrome, remove padding ─────────────────────────────────────
st.markdown("""
<style>
  header[data-testid="stHeader"]  { display: none !important; }
  .block-container                 { padding: 0 !important; max-width: 100% !important; }
  [data-testid="stAppViewContainer"] > section > div { padding: 0 !important; }
</style>
""", unsafe_allow_html=True)

# ── Build self-contained HTML document (inlines CSS) ─────────────────────────
# This avoids Streamlit's HTML sanitiser stripping <section>, <article>, etc.
full_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap"
        rel="stylesheet"/>
  <style>{css_content}</style>
</head>
<body>
{html_content}
</body>
</html>"""

# ── Render inside a full-height iframe ───────────────────────────────────────
components.html(full_page, height=5800, scrolling=True)

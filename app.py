"""
app.py — Streamlit Resume App for Ashutosh Sharma
Run locally : streamlit run app.py
Deploy      : Push to GitHub → connect to Streamlit Cloud
"""

import streamlit as st
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
    st.markdown("""
- [🏠 Home](#home)
- [🙋 About Me](#about)
- [🛠️ Skills](#skills)
- [📁 Projects](#projects)
- [🎓 Education](#education)
- [📬 Contact](#contact)
""", unsafe_allow_html=True)

    st.divider()

    st.markdown("### 📬 Quick Contact")
    st.markdown("📧 sharma.ashutosh.work@gmail.com")
    st.markdown("📞 +91 92840 73347")

    st.divider()

    st.markdown("### 🌐 Links")
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("LinkedIn", "https://linkedin.com/in/ashutosh-sharma-in", use_container_width=True)
    with col2:
        st.link_button("GitHub", "https://github.com/SharmaAshuu", use_container_width=True)

    st.divider()
    st.caption("Built with Streamlit · 2024")

# ── Inject CSS + render HTML ─────────────────────────────────────────────────
# Embed the external CSS inline so Streamlit Cloud doesn't need to serve it
st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

# Remove default Streamlit padding so the hero fills edge-to-edge
st.markdown("""
<style>
  /* Remove Streamlit's default page padding */
  .block-container { padding: 0 !important; max-width: 100% !important; }
  header[data-testid="stHeader"] { display: none; }
  /* Scrollable anchor support */
  html { scroll-behavior: smooth; }
</style>
""", unsafe_allow_html=True)

# Render the full HTML resume
st.markdown(html_content, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="
  text-align:center;
  padding: 14px;
  font-family: 'Poppins', sans-serif;
  font-size: .78rem;
  color: #888;
  border-top: 1px solid #e5e7eb;
  margin-top: 0;
">
  © Ashutosh Sharma · Data Analyst · Pune, India
</div>
""", unsafe_allow_html=True)

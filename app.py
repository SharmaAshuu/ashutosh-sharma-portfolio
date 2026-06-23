"""
app.py — Streamlit Resume App for Ashutosh Sharma
Run: streamlit run app.py
"""

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Ashutosh Sharma | Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

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
    for icon, label, anchor in [
        ("🏠","Home","home"), ("🙋","About Me","about"),
        ("🛠️","Skills","skills"), ("📁","Projects","projects"),
        ("🎓","Education","education"), ("📬","Contact","contact"),
    ]:
        st.markdown(
            f'<a href="#{anchor}" style="display:block;padding:8px 14px;margin:3px 0;'
            f'background:#f0eff8;border-radius:8px;text-decoration:none;color:#3b0080;'
            f'font-family:Poppins,sans-serif;font-size:0.88rem;font-weight:500;">'
            f'{icon} {label}</a>',
            unsafe_allow_html=True,
        )
    st.divider()
    st.markdown("### 📬 Quick Contact")
    st.markdown("📧 sharma.ashutosh.work@gmail.com")
    st.markdown("📞 +91 92840 73347")
    st.divider()
    st.markdown("### 🌐 Links")
    c1, c2 = st.columns(2)
    c1.link_button("LinkedIn", "https://linkedin.com/in/ashutosh-sharma-in", use_container_width=True)
    c2.link_button("GitHub",   "https://github.com/SharmaAshuu",            use_container_width=True)
    st.divider()
    st.caption("© Ashutosh Sharma · Streamlit")

# ── Strip ALL Streamlit chrome & padding ─────────────────────────────────────
st.markdown("""
<style>
  header[data-testid="stHeader"] { display:none !important; }
  footer                          { display:none !important; }
  .block-container                { padding:0 !important; max-width:100% !important; }
  section.main > div              { padding:0 !important; }
  [data-testid="stAppViewContainer"] > section { padding:0 !important; }
  iframe                          { display:block; border:none; width:100% !important; }
</style>
""", unsafe_allow_html=True)

# ── Build full self-contained document ───────────────────────────────────────
full_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet"/>
  <style>
    *{{box-sizing:border-box;margin:0;padding:0;}}
    html,body{{margin:0;padding:0;overflow-x:hidden;width:100%;height:100%;}}
    {css_content}
  </style>
</head>
<body>
{html_content}
</body>
</html>"""

# height=9500 covers all sections; scrolling=True lets user scroll inside
# Auto-fit height for desktop/laptop
components.html(
    full_page,
    height=1200,
    scrolling=True
)

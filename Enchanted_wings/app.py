import streamlit as st
import streamlit as st
from utils.style import apply_global_styles

st.set_page_config(page_title="Enchanted Wings", page_icon="🦋", layout="wide")
apply_global_styles()

st.markdown("""
<style>
/* General page styling */
body {
    background: linear-gradient(to right, #fce4ec, #e0f7fa);
    font-family: 'Segoe UI', sans-serif;
    color: #333;
}

/* NAVBAR */
.navbar {
    background-color: #ffffffcc;
    padding: 1rem 2rem;
    border-bottom: 1px solid #e1bee7;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: sticky;
    top: 0;
    z-index: 999;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}
.navbar h2 {
    color: #6a1b9a;
    margin: 0;
    font-weight: bold;
}
.navbar a {
    color: #8e24aa;
    margin-left: 1.8rem;
    text-decoration: none;
    font-weight: 600;
    font-size: 16px;
}
.navbar a:hover {
    color: #4a148c;
    border-bottom: 2px solid #6a1b9a;
}

/* HERO SECTION */
.hero {
    padding: 4rem 2rem 2rem;
    background: linear-gradient(135deg, #f3e5f5 30%, #e1f5fe 100%);
    border-radius: 25px;
    margin: 2rem auto;
    box-shadow: 0 8px 24px rgba(0,0,0,0.1);
    max-width: 1000px;
    text-align: center;
}
.hero h1 {
    font-size: 3rem;
    color: #6a1b9a;
    font-weight: 800;
}
.hero p {
    font-size: 1.2rem;
    color: #444;
    margin-top: 1rem;
    max-width: 700px;
    margin: auto;
}
.hero .stButton>button {
    margin-top: 2rem;
    background-color: #8e24aa;
    color: white;
    font-size: 1.1rem;
    padding: 0.8rem 2rem;
    border-radius: 12px;
    font-weight: bold;
    box-shadow: 0 5px 15px rgba(142,36,170,0.3);
    transition: all 0.3s ease;
}
.hero .stButton>button:hover {
    background-color: #6a1b9a;
    transform: scale(1.07);
}

/* Sidebar Styling */
section[data-testid="stSidebar"] {
    background-color: #f3e5f5;
    border-right: 2px solid #ce93d8;
    padding-top: 2rem;
}
.css-1d391kg {
    color: #6a1b9a !important;
    font-weight: bold;
}

/* Footer */
.footer {
    margin-top: 6rem;
    text-align: center;
    font-size: 0.85rem;
    color: #777;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="navbar">
    <h2>🦋 Enchanted Wings</h2>
   
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero">
    <h1>Explore the Marvels of Butterfly Species</h1>
    <p>Upload a butterfly image and our AI will tell you its species. Dive into a magical world of color, science, and nature.</p>
</div>
""", unsafe_allow_html=True)

st.button("🦋 Get Started")

st.write("👈 Use the sidebar to navigate or upload butterfly images.")

st.markdown("""
<div class="footer">
    © 2025 Enchanted Wings · Powered by AI & Nature · Designed with 💜 using Streamlit
</div>
""", unsafe_allow_html=True)

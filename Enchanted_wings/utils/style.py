import streamlit as st

def apply_global_styles():
    st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        color: #2c2c2c;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(to bottom, #f3e5f5, #e1f5fe);
        border-right: 2px solid #ce93d8;
        padding-top: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
        box-shadow: 2px 0 6px rgba(0,0,0,0.05);
        position: relative;
    }

    .sidebar-logo {
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 1rem;
        width: 120px;
        border-radius: 50%;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        border: 3px solid #ce93d8;
    }

    .sidebar-title {
        text-align: center;
        color: #6a1b9a;
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 2rem;
    }

    [data-testid="stSidebarNav"] li {
        padding: 0.5rem 0.75rem;
        margin-bottom: 0.3rem;
        border-radius: 8px;
        transition: background-color 0.2s ease;
    }

    [data-testid="stSidebarNav"] li:hover {
        background-color: #fce4ec;
    }

    [data-testid="stSidebarNav"] a {
        color: #6a1b9a;
        font-weight: 600;
        font-size: 15px;
        text-decoration: none;
    }

    [data-testid="stSidebarNav"] a:hover {
        color: #4a148c;
    }

    h1, h2, h3 {
        color: #6a1b9a;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    st.sidebar.markdown(
        """
        <img src="https://wildhawk.in/wp-content/uploads/2022/10/butter.jpg" class="sidebar-logo" />
        <div class="sidebar-title">Enchanted Wings</div>
        """,
        unsafe_allow_html=True
    )

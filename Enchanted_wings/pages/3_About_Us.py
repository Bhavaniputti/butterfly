import streamlit as st
from utils.style import apply_global_styles

st.set_page_config(page_title="Enchanted Wings", page_icon="🦋", layout="wide")
apply_global_styles()
st.markdown("<h2 style='color: #6a1b9a;'>👥 Meet the Team</h2>", unsafe_allow_html=True)

team = [
    {"name": "Bhavani Putti", "role": "Team Leader"},
    {"name": "Chollangi Bharath Sai", "role": "Member"},
    {"name": "Bhavana Tamarapu", "role": "Member"},
    {"name": "Chakravartula Ananta Satish", "role": "Member"}
]

for member in team:
    st.markdown(f"""
    <div style='padding: 10px; background-color: #f0e8f9; border-radius: 10px; margin-bottom: 10px;'>
        <b>{member['name']}</b><br>
        <i>{member['role']}</i>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<hr>
<center>Team ID: <b>LTVIP2025TMID44685</b></center>
""", unsafe_allow_html=True)

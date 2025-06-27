import streamlit as st
from utils.style import apply_global_styles

st.set_page_config(page_title="Enchanted Wings", page_icon="🦋", layout="wide")
apply_global_styles()

st.markdown("""
<style>
.welcome-title {
    text-align: center;
    font-size: 2.5rem;
    font-weight: bold;
    color: #6a1b9a;
    margin-top: 2rem;
    text-shadow: 1px 1px 2px #e1bee7;
}
.feature-box {
    background: #f8bbd0;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    margin-top: 2rem;
    font-size: 1.05rem;
    color: #4a148c;
}
.feature-box li {
    margin-bottom: 1rem;
}
.instructions {
    margin-top: 2rem;
    font-size: 1.1rem;
    color: #555;
    background-color: #fff3e0;
    padding: 1.5rem;
    border-radius: 15px;
    border-left: 5px solid #ffb74d;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
.center-text {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='welcome-title'>🦋 Welcome to Enchanted Wings!</div>", unsafe_allow_html=True)

st.markdown("""
<div class='center-text' style='margin-top: 1rem; font-size: 1.1rem; color: #444;'>
An AI-powered butterfly species classifier that blends <b>nature</b> with <b>neural networks</b>.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='feature-box'>
    <ul>
        <li>🧠 <strong>AI Model:</strong> Predict butterfly species using a trained deep learning model.</li>
        <li>🌼 <strong>Clean UI:</strong> Beautiful, simple, and intuitive interface for easy use.</li>
        <li>📷 <strong>Upload Friendly:</strong> Upload your own butterfly photo and get instant predictions.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='instructions'>
👉 Use the <strong>sidebar</strong> to navigate between pages like <em>Prediction</em> and <em>About the Team</em>.  
📥 Start by heading to the <strong>Prediction</strong> tab and uploading a butterfly image.  
📊 You’ll get the predicted species with confidence level in seconds!
</div>
""", unsafe_allow_html=True)

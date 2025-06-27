import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import json
from PIL import Image
from utils.style import apply_global_styles

st.set_page_config(page_title="Enchanted Wings", page_icon="🦋", layout="wide")
apply_global_styles()
model = load_model("butterfly_classifier.h5")
IMAGE_SIZE = (100, 100)

with open("class_indices.json", "r") as f:
    class_indices = json.load(f)
class_names = {v: k for k, v in class_indices.items()}



st.markdown("""
<style>
.result-box {
    background: rgba(255, 255, 255, 0.65);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    padding: 2rem;
    margin-top: 2rem;
    box-shadow: 0 8px 30px rgba(0,0,0,0.1);
    text-align: center;
}
.result-box h2 {
    color: #388e3c;
}
.result-box h1 {
    color: #1e88e5;
    margin: 1rem 0 0.5rem;
}
.footer {
    text-align: center;
    font-size: 13px;
    color: gray;
    margin-top: 3rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🦋 Enchanted Wings</h1>", unsafe_allow_html=True)
st.markdown("<h3>Butterfly Species Predictor</h3>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("📸 Upload a butterfly image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="🖼️ Uploaded Image", use_container_width=True)
    img_resized = img.resize(IMAGE_SIZE)
    img_array = image.img_to_array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    with st.spinner("🔍 Predicting the species..."):
        prediction = model.predict(img_array)
        predicted_class = class_names[np.argmax(prediction)]
        confidence = float(np.max(prediction)) * 100

    st.markdown(f"""
    <div class="result-box">
        <h2>🧠 Prediction:</h2>
        <h1>{predicted_class}</h1>
        <p>Confidence: <b>{confidence:.2f}%</b></p>
        <p>🧬 Learn more about <b>{predicted_class}</b> in the Explore tab.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔁 Try Another Image"):
        st.experimental_rerun()
else:
    st.info("Please upload a butterfly image to get started.")

st.markdown("<div class='footer'>Made with 💜 by Team Enchanted Wings</div>", unsafe_allow_html=True)

import streamlit as st

st.set_page_config(page_title="Cyber Fraud Detector", page_icon="🛡️", layout="centered")

st.markdown("<h1 style='text-align: center; color: red;'>🛡️ Cyber Fraud Detection System</h1>", unsafe_allow_html=True)

st.markdown("### Enter transaction details below 👇")

amount = st.number_input("💰 Transaction Amount", min_value=0)
time = st.number_input("⏰ Time (0–23)", min_value=0, max_value=23)
location = st.selectbox("📍 Location Risk", ["Low", "High"])

if st.button("🚀 Predict"):
    if amount > 50000:
        st.error("⚠️ Fraud Detected!")
    else:
        st.success("✅ Safe Transaction")

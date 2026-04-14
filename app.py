import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Cyber Fraud Detector", page_icon="🛡️", layout="centered")

st.markdown("<h1 style='text-align: center; color: red;'>🛡️ Cyber Fraud Detection System</h1>", unsafe_allow_html=True)

st.markdown("### Enter transaction details below 👇")

amount = st.number_input("💰 Transaction Amount", min_value=0)
time = st.number_input("⏰ Time (0–23)", min_value=0, max_value=23)
location = st.selectbox("📍 Location Risk", ["Low", "High"])

prediction = None
result_text = ""

if st.button("🚀 Predict"):
    if amount > 50000:
        prediction = 1
        result_text = "Fraud"
        st.error("⚠️ Fraud Detected!")
    else:
        prediction = 0
        result_text = "Safe"
        st.success("✅ Safe Transaction")

    # 📊 Graph
    st.subheader("Fraud vs Safe Graph")

    fraud_count = 30
    safe_count = 70

    labels = ['Fraud', 'Safe']
    values = [fraud_count, safe_count]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title("Fraud vs Safe Transactions")
    ax.set_ylabel("Count")

    st.pyplot(fig)

    # 📥 Download result
    df = pd.DataFrame({
        "Amount": [amount],
        "Time": [time],
        "Location": [location],
        "Result": [result_text]
    })

    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="📥 Download Result",
        data=csv,
        file_name='result.csv',
        mime='text/csv'
    )

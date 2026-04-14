import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

st.set_page_config(page_title="Cyber Fraud Detector", page_icon="🛡️", layout="centered")

st.markdown("<h1 style='text-align: center; color: red;'>🛡️ Cyber Fraud Detection System</h1>", unsafe_allow_html=True)

st.markdown("### Enter transaction details below 👇")

# 📊 Sample Dataset (Training Data)
data = {
    'amount': [100, 5000, 200, 70000, 150, 90000, 300],
    'time': [10, 23, 14, 2, 16, 1, 12],
    'location_risk': [0, 1, 0, 1, 0, 1, 0],
    'fraud': [0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

X = df[['amount', 'time', 'location_risk']]
y = df['fraud']

# 🤖 Train Model
model = LogisticRegression()
model.fit(X, y)

# 🎯 User Input
amount = st.number_input("💰 Transaction Amount", min_value=0)
time = st.number_input("⏰ Time (0–23)", min_value=0, max_value=23)
location = st.selectbox("📍 Location Risk", ["Low", "High"])

loc_val = 1 if location == "High" else 0

if st.button("🚀 Predict"):
    
    prediction = model.predict([[amount, time, loc_val]])

    if prediction[0] == 1:
        result_text = "Fraud"
        st.error("⚠️ Fraud Detected!")
    else:
        result_text = "Safe"
        st.success("✅ Safe Transaction")

    # 📊 Graph
    st.subheader("Fraud vs Safe Graph")

    labels = ['Fraud', 'Safe']
    values = [40, 60]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    st.pyplot(fig)

    # 📥 Download Result
    result_df = pd.DataFrame({
        "Amount": [amount],
        "Time": [time],
        "Location": [location],
        "Result": [result_text]
    })

    csv = result_df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="📥 Download Result",
        data=csv,
        file_name='result.csv',
        mime='text/csv'
    )

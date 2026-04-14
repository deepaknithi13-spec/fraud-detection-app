import streamlit as st
# --- LOGIN SYSTEM ---
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if username != "cyberstorm" or password != "1234":
    st.warning("Enter correct login details")
    st.stop()
    st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
    }
    .stApp {
        background: linear-gradient(to right, #141e30, #243b55);
        color: white;
    }
    h1 {
        text-align: center;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)
import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

st.set_page_config(page_title="Cyber Fraud Detector", page_icon="🛡️", layout="centered")

st.markdown("""
<div style='background-color:#ff4b4b;padding:15px;border-radius:10px'>
<h1 style='text-align:center;color:white;'>🛡️ Cyber Fraud Detection System</h1>
</div>
""", unsafe_allow_html=True)
st.markdown("### Enter transaction details below 👇")
st.write("")
st.write("")

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
st.subheader("Enter Details")

col1, col2 = st.columns(2)

with col1:
    amount = st.number_input("Transaction Amount", min_value=0)

with col2:
    time = st.number_input("Time (0–23)", min_value=0, max_value=23)

location = st.selectbox("Location Risk", ["Low", "High"])

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
    st.markdown("---")
st.markdown("Cyber Storm Guard ⚡ | Cyber Security Project")

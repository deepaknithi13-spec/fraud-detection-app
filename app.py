import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Cyber Fraud Detector", layout="centered")

st.markdown("<h1 style='text-align: center; color: red;'>Cyber Fraud Detection System</h1>", unsafe_allow_html=True)

st.markdown("### Enter transaction details below")

# Inputs
amount = st.number_input("Enter Transaction Amount", min_value=0)
time = st.number_input("Enter Time (0-23)", min_value=0, max_value=23)
location = st.selectbox("Location Risk", ["Low", "High"])

prediction = ""
result_text = ""

# Prediction Button
if st.button("Predict Fraud"):
    if amount > 50000 or location == "High":
        prediction = "Fraud"
        st.error("Fraud Detected!")
    else:
        prediction = "Normal"
        st.success("Safe Transaction")

# Graph
st.subheader("Fraud vs Normal Graph")

labels = ['Fraud', 'Normal']
values = [30, 70]

fig, ax = plt.subplots()
ax.bar(labels, values)
ax.set_title("Fraud vs Normal Transactions")

st.pyplot(fig)

# Download Section
st.subheader("Download Result")

df = pd.DataFrame({
    "Amount": [amount],
    "Time": [time],
    "Location": [location],
    "Prediction": [prediction]
})

csv = df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download Result as CSV",
    data=csv,
    file_name="fraud_result.csv",
    mime="text/csv"
)

st.write("APP UPDATED SUCCESSFULLY")
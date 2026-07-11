import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Phishing Email Detection",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Phishing Email Detection Model")
st.write("Machine Learning Internship Project")

# Load model
try:
    model = joblib.load("phishing_model.pkl")
except:
    st.error("Model not found! Please train the model first.")
    st.stop()

menu = st.sidebar.selectbox(
    "Select",
    [
        "Problem Statement",
        "Dataset",
        "Detect Email",
        "About Project"
    ]
)

if menu == "Problem Statement":

    st.header("Problem Statement")

    st.write("""
Phishing emails are designed to steal sensitive information such as passwords,
bank details, and personal information.

Machine Learning can automatically classify emails as
**Phishing** or **Legitimate**, helping users identify suspicious emails.
""")

elif menu == "Dataset":

    st.header("Email Dataset")

    df = pd.read_csv("emails.csv")

    st.dataframe(df)

    st.write("### Dataset Columns")

    st.write("**text** → Email Content")

    st.write("**label** → phishing / legitimate")

elif menu == "Detect Email":

    st.header("Email Detection")

    email = st.text_area("Enter Email")

    if st.button("Predict"):

        prediction = model.predict([email])[0]

        if prediction.lower() == "phishing":
            st.error("⚠️ Prediction : PHISHING EMAIL")
        else:
            st.success("✅ Prediction : LEGITIMATE EMAIL")

elif menu == "About Project":

    st.header("Project Workflow")

    st.markdown("""
1. Collect Email Dataset

2. Preprocess Email Text

3. Convert Text using TF-IDF

4. Train Naive Bayes Model

5. Save Trained Model

6. User Enters Email

7. Predict Phishing / Legitimate

8. Display Result
""")

st.sidebar.success("Cyber Security Internship Project")
pip install streamlit pandas scikit-learn joblib
streamlit run app.py
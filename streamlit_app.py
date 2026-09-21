import os
import joblib
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Isaiah Mposhomali : Credit Risk Modelling Project",
    page_icon="💳",
    layout="wide"
)

# =====================================================
# CUSTOM CSS (kept minimal on purpose)
# =====================================================
st.markdown("""
<style>
.stButton > button {
    background-color: #2563eb;
    color: white !important;
    border-radius: 12px;
    height: 3.2em;
    width: 100%;
    font-size: 18px;
    font-weight: 600;
    border: none;
}
.stButton > button:hover { background-color: #1d4ed8; }
.section-card {
    background-color: white;
    padding: 20px;
    border-radius: 14px;
    margin-bottom: 20px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# PATHS
# NOTE: This file must live at the repo root (same folder
# as the "models" and "assets" folders) for this to work
# on Streamlit Community Cloud.
# =====================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "logistic_regression.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")
IMAGE_PATH = os.path.join(BASE_DIR, "assets", "finance.jpg")

# =====================================================
# LOAD MODEL + SCALER (fail loudly but cleanly)
# =====================================================
@st.cache_resource
def load_artifacts():
    if not os.path.exists(MODEL_PATH):
        st.error(f"Model file not found at: {MODEL_PATH}")
        st.stop()
    if not os.path.exists(SCALER_PATH):
        st.error(f"Scaler file not found at: {SCALER_PATH}")
        st.stop()
    return joblib.load(MODEL_PATH), joblib.load(SCALER_PATH)

model, scaler = load_artifacts()

# =====================================================
# SIDEBAR
# =====================================================
with st.sidebar:
    st.title("Instructions")

    if os.path.exists(IMAGE_PATH):
        st.image(IMAGE_PATH, width=250)

    st.markdown("""
    ### Steps
    1. Enter customer details
    2. Adjust loan information
    3. Click **Predict Credit Risk**
    4. Review risk insights
    """)
    st.markdown("---")
    st.info("This app uses Logistic Regression for credit risk scoring.")

# =====================================================
# TITLE
# =====================================================
st.title("💳 Isaiah Mposhomali : Credit Risk Modelling")
st.markdown("### Credit Risk Assessment")

# =====================================================
# CUSTOMER DETAILS
# =====================================================
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown("## 👤 Customer Details")

col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input("Age", min_value=18, max_value=75, value=30)
with col2:
    credit_amount = st.slider("Credit Amount", 1000, 1000000, 50000, step=5000)
    st.markdown(f"**Selected Loan Amount: R{credit_amount:,.0f}**")
with col3:
    duration = st.number_input("Loan Duration (Months)", min_value=4, max_value=72, value=24)

st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# LOAN + FINANCIAL DETAILS
# =====================================================
st.markdown("## 🏦 Loan & Financial Details")

col4, col5, col6 = st.columns(3)
with col4:
    sex = st.selectbox("Sex", ["male", "female"])
with col5:
    housing = st.selectbox("Housing", ["own", "rent", "free"])
with col6:
    purpose = st.selectbox("Purpose", ["car", "radio/TV", "education", "furniture/equipment", "business"])

col7, col8, col9 = st.columns(3)
with col7:
    saving_accounts = st.selectbox("Saving Accounts", ["little", "moderate", "quite rich", "rich"])
with col8:
    checking_account = st.selectbox("Checking Account", ["little", "moderate", "rich"])
with col9:
    job = st.selectbox("Job Level", [0, 1, 2, 3])

# =====================================================
# ENCODING MAPS
# =====================================================
SEX_MAP = {"male": 1, "female": 0}
HOUSING_MAP = {"own": 0, "rent": 1, "free": 2}
SAVING_MAP = {"little": 0, "moderate": 1, "quite rich": 2, "rich": 3}
CHECKING_MAP = {"little": 0, "moderate": 1, "rich": 2}
PURPOSE_MAP = {"car": 0, "radio/TV": 1, "education": 2, "furniture/equipment": 3, "business": 4}

# =====================================================
# BUILD INPUT DATAFRAME
# =====================================================
input_data = pd.DataFrame({
    "Age": [age],
    "Sex": [SEX_MAP[sex]],
    "Job": [job],
    "Housing": [HOUSING_MAP[housing]],
    "Saving accounts": [SAVING_MAP[saving_accounts]],
    "Checking account": [CHECKING_MAP[checking_account]],
    "Credit amount": [credit_amount],
    "Duration": [duration],
    "Purpose": [PURPOSE_MAP[purpose]]
})

feature_cols = input_data.columns.tolist()
input_data[feature_cols] = scaler.transform(input_data[feature_cols])

# =====================================================
# PREDICT
# =====================================================
st.markdown("---")

if st.button("Predict Credit Risk"):

    probability = model.predict_proba(input_data)[0][1]
    prediction = model.predict(input_data)[0]

    if probability < 0.3:
        risk_level = "Low Risk 🟢"
    elif probability < 0.7:
        risk_level = "Medium Risk 🟠"
    else:
        risk_level = "High Risk 🔴"

    st.markdown("## 📊 Prediction Summary")
    m1, m2, m3 = st.columns(3)
    m1.metric("Risk Probability", f"{probability:.2%}")
    m2.metric("Risk Category", risk_level)
    m3.metric("Prediction", "Bad Credit" if prediction == 1 else "Good Credit")

    tab1, tab2, tab3 = st.tabs(["Prediction", "Feature Importance", "Model Metrics"])

    # ---------------- TAB 1: PREDICTION ----------------
    with tab1:
        if prediction == 1:
            st.error("🔴 High Risk Customer")
        else:
            st.success("🟢 Low Risk Customer")

        st.markdown("### Customer Summary")
        summary_df = pd.DataFrame({
            "Feature": ["Age", "Credit Amount", "Duration", "Housing", "Purpose"],
            "Value": [age, credit_amount, duration, housing, purpose]
        })
        st.table(summary_df)

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=probability * 100,
            title={'text': "Risk Score"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "darkred"},
                'steps': [
                    {'range': [0, 30], 'color': "lightgreen"},
                    {'range': [30, 70], 'color': "orange"},
                    {'range': [70, 100], 'color': "red"}
                ]
            }
        ))
        st.plotly_chart(fig, use_container_width=True)

        st.info("""
        • Higher credit amounts are associated with higher default risk.
        • Low checking account balances tend to show elevated risk.
        • Longer loan durations increase likelihood of bad credit classification.
        • Housing and savings behavior influence the prediction.
        """)

    # ---------------- TAB 2: FEATURE IMPORTANCE ----------------
    with tab2:
        importance_df = pd.DataFrame({
            "Feature": input_data.columns,
            "Importance": model.coef_[0]
        }).sort_values("Importance")

        fig_imp = px.bar(
            importance_df, x="Importance", y="Feature",
            orientation="h", title="Logistic Regression Coefficients"
        )
        st.plotly_chart(fig_imp, use_container_width=True)

    # ---------------- TAB 3: MODEL METRICS ----------------
    with tab3:
        c1, c2, c3 = st.columns(3)
        c1.metric("Accuracy", "42.11%")
        c2.metric("ROC-AUC", "0.5043")
        c3.metric("Model Status", "Near chance")
        st.caption(
            "The Logistic Regression model shows 42.11% accuracy and 0.5043 ROC-AUC, "
            "which indicates performance close to chance level."
        )

# =====================================================
# DOWNLOAD
# =====================================================
st.markdown("---")
download_data = pd.DataFrame({
    "Age": [age], "Sex": [sex], "Job Level": [job], "Housing": [housing],
    "Saving Accounts": [saving_accounts], "Checking Account": [checking_account],
    "Credit Amount": [credit_amount], "Duration": [duration], "Purpose": [purpose]
})

st.download_button(
    label="Download Prediction Data",
    data=download_data.to_csv(index=False),
    file_name="credit_risk_prediction.csv",
    mime="text/csv"
)

# =====================================================
# FOOTER
# =====================================================
st.markdown("---")
st.markdown("""
### ⚙️ Technology Stack
- Python · Streamlit · Logistic Regression · Machine Learning
""")

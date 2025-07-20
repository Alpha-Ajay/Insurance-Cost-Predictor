import streamlit as st
import pickle
import numpy as np

# 0. Page config
st.set_page_config(
    page_title="Insurance Cost Predictor",
    page_icon="💡",
    layout="wide",
)

# 1. Load model
model = pickle.load(open('insurance_model.pkl', 'rb'))

# 2. Sidebar for inputs
st.sidebar.header("👤 User Inputs")
sex = st.sidebar.selectbox("Sex", ["male", "female"])
children = st.sidebar.number_input("Number of Children", 0, 10, 0)
smoker = st.sidebar.selectbox("Smoker?", ["yes", "no"])
claim_amount = st.sidebar.number_input("Claim Amount", 0.0, 100000.0, 1000.0, step=500.0)
past_consultations = st.sidebar.number_input("Past Consultations", 0, 20, 2)
hospital_expenditure = st.sidebar.number_input("Hospital Expenditure", 0.0, 500000.0, 5000.0, step=1000.0)
anual_salary = st.sidebar.number_input("Annual Salary", 0.0, 1000000.0, 50000.0, step=5000.0)
region = st.sidebar.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

st.sidebar.markdown("---")
predict_btn = st.sidebar.button("🚀 Predict Charges")

# 3. Main title
st.title("💡 Insurance Cost Prediction")
st.markdown(
    "Use the form on the left to enter your details and get an estimated insurance premium."
)

# 4. Encode inputs
sex_encoded    = 1 if sex == "male" else 0
smoker_encoded = 1 if smoker == "yes" else 0
region_map     = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}
region_encoded = region_map[region]

# 5. Prediction logic
if predict_btn:
    features = np.array([[ 
        sex_encoded,
        children,
        smoker_encoded,
        claim_amount,
        past_consultations,
        hospital_expenditure,
        anual_salary,
        region_encoded
    ]])
    pred = model.predict(features)[0]

    # 6. Display result in a column layout
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("🔍 Prediction Results")
        st.write(f"Based on your inputs, your estimated insurance charge is:")
    with col2:
        st.metric(label="💰 Estimated Charge", value=f"₹ {pred:,.2f}")

    st.markdown("---")
    st.write("**Model used:** Linear Regression  \n"
             "**R² Score:** 0.85 (85%)")

# 7. Footer / credit
st.markdown(
    "<br><hr><p style='font-size:0.8em;'>Built with Streamlit • Model trained on Kaggle Medical Insurance dataset</p>",
    unsafe_allow_html=True
)

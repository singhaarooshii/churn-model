import streamlit as st
import pickle
import pandas as pd

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="🏦",
    layout="wide"
)

# ---------------- Load Model ----------------
model = pickle.load(open("churn_model.pkl", "rb"))

# ---------------- Custom CSS ----------------
st.markdown("""
<style>

.main{
    background-color:#f5f7fa;
}

h1{
    color:#004aad;
    text-align:center;
}

.stButton>button{
    background:#004aad;
    color:white;
    border-radius:10px;
    width:100%;
    height:3em;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#0066ff;
}

div[data-testid="stMetric"]{
    background:#ffffff;
    border-radius:10px;
    padding:10px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.2);
}
div[data-baseweb="input"] input {
    color: black !important;
    background: white !important;
    font-weight: bold !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Title ----------------
st.title("🏦 Customer Churn Prediction")
st.markdown(
    "<h4 style='text-align:center;color:grey;'>Predict whether a customer will stay or leave the bank.</h4>",
    unsafe_allow_html=True
)

st.divider()

# ---------------- Sidebar ----------------
st.sidebar.header("📋 Customer Information")

credit_score = st.sidebar.number_input("Credit Score",300,900,650)

geography = st.sidebar.selectbox(
    "Geography",
    ["France","Germany","Spain"]
)

gender = st.sidebar.selectbox(
    "Gender",
    ["Female","Male"]
)

age = st.sidebar.number_input(
    "Age",
    18,100,35
)

tenure = st.sidebar.number_input(
    "Tenure",
    0,10,5
)

balance = st.sidebar.number_input(
    "Balance",
    value=50000.0
)

num_products = st.sidebar.number_input(
    "Number of Products",
    1,4,1
)

has_card = st.sidebar.selectbox(
    "Has Credit Card",
    [0,1]
)

active_member = st.sidebar.selectbox(
    "Is Active Member",
    [0,1]
)

salary = st.sidebar.number_input(
    "Estimated Salary",
    value=50000.0
)

# ---------------- Encoding ----------------
gender = 1 if gender=="Male" else 0

geo_france = 1 if geography=="France" else 0
geo_germany = 1 if geography=="Germany" else 0
geo_spain = 1 if geography=="Spain" else 0

# ---------------- Metrics ----------------
col1,col2,col3 = st.columns(3)

col1.metric("💳 Credit Score",credit_score)
col2.metric("👤 Age",age)
col3.metric("💰 Balance",balance)

st.progress(100)

# ---------------- Prediction ----------------
if st.button("🔍 Predict Customer Churn"):

    data = pd.DataFrame({
        "CreditScore":[credit_score],
        "Gender":[gender],
        "Age":[age],
        "Tenure":[tenure],
        "Balance":[balance],
        "NumOfProducts":[num_products],
        "HasCrCard":[has_card],
        "IsActiveMember":[active_member],
        "EstimatedSalary":[salary],
        "Geography_France":[geo_france],
        "Geography_Germany":[geo_germany],
        "Geography_Spain":[geo_spain]
    })

    prediction = model.predict(data)

    st.divider()

    if prediction[0]==1:
        st.error("⚠️ Customer is likely to leave the bank.")
    else:
        st.success("✅ Customer is likely to stay with the bank.")


   

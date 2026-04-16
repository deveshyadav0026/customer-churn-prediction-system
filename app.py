import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Customer Churn Prediction", layout="wide")

# -------------------------------
# LOAD MODEL
# -------------------------------
@st.cache_resource
def load_model():
    model = joblib.load("model.pkl")
    return model

model = load_model()

# -------------------------------
# TITLE
# -------------------------------
st.title("📊 Customer Churn Prediction System")
st.markdown("Predict whether a customer will churn and take business actions.")

# -------------------------------
# SIDEBAR INPUTS
# -------------------------------
st.sidebar.header("Enter Customer Details")

tenure = st.sidebar.slider("Tenure (months)", 0, 72, 1)
warehouse_to_home = st.sidebar.slider("Warehouse to Home Distance (KM)", 1, 50, 10)
day_since_last_order = st.sidebar.slider("Days Since Last Order", 0, 365, 30)
satisfaction = st.sidebar.slider("Satisfaction Score", 1, 5, 4)
devices = st.sidebar.slider("Number of Devices", 1, 10, 5)
addresses = st.sidebar.slider("Number of Addresses", 1, 10, 5)
cashback = st.sidebar.number_input("Cashback Amount", 0, 1000, 1)

# Categorical
marital_status = st.sidebar.selectbox("Marital Status", ["Single", "Married","Divorced"])
complain = st.sidebar.selectbox("Complain", [0, 1])
selected_category = st.sidebar.selectbox("Preferred Order Category", ["Laptop & Accessory", "Watch", "Fashion", "Grocery","Mobile Phone", "Other" ])

# -------------------------------
# CREATE INPUT DATAFRAME
# -------------------------------


columns = joblib.load("columns.pkl")
input_data = pd.DataFrame([[0]*len(columns)],columns=columns)

input_data.loc[0, 'Tenure'] = tenure
input_data.loc[0, 'WarehouseToHome'] = warehouse_to_home
input_data.loc[0, 'DaySinceLastOrder'] = day_since_last_order

# Encoding (safe)

input_data.loc[0, 'MaritalStatus_single'] = 1 if marital_status == "Single" else 0
input_data.loc[0, 'MaritalStatus_married'] = 1 if marital_status == "Married" else 0
input_data.loc[0, 'MaritalStatus_divorced'] = 1 if marital_status == "Divorced" else 0

input_data.loc[0, 'SatisfactionScore'] = satisfaction
input_data.loc[0, 'NumberOfDeviceRegistered'] = devices
input_data.loc[0, 'NumberOfAddress'] = addresses
input_data.loc[0, 'CashbackAmount'] = cashback

category = selected_category  # from dropdown

col_name = f"PreferredOrderCat_{category}"

if col_name in input_data.columns:
    input_data.loc[0, col_name] = 1


input_data.loc[0, 'Complain'] = complain

# Fill missing columns
input_data = input_data.fillna(0)






# -------------------------------
# PREDICTION
# -------------------------------
if st.button("Predict Churn"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    threshold = 0.5
    prediction = 1 if probability > threshold else 0
    percentage = probability*100

    st.subheader("📈 Prediction Result")

    if prediction == 1:
        st.error(f"⚠️ Customer is likely to CHURN")
    else:
        st.success(f"✅ Customer is NOT likely to churn")

    st.write(f"**Churn Percentage:** {percentage:.2f}%")

    # -------------------------------
    # RISK LEVEL
    # -------------------------------
    if percentage > 50:
        risk = "High Risk 🔴"
    elif percentage > 7:
        risk = "Medium Risk 🟡"
    else:
        risk = "Low Risk 🟢"

    st.write(f"**Risk Level:** {risk}")

    # -------------------------------
    # BUSINESS ACTIONS
    # -------------------------------
    st.subheader("💡 Recommended Actions")

    if percentage > 50:
        st.write("- Offer heavy discount")
        st.write("- Assign relationship manager")
        st.write("- Personalized retention call")

    elif percentage > 7:
        st.write("- Send targeted offers")
        st.write("- Improve engagement (notifications/email)")
    
    else:
        st.write("- Maintain service quality")
        st.write("- Upsell premium products")

# -------------------------------
# EDA SECTION
# -------------------------------
st.markdown("---")
st.header("📊 Exploratory Data Insights")

st.write("""
### Key Insights:
- Customers with **high days since last order** are more likely to churn
- Low **tenure customers** churn more frequently
- Complaints strongly increase churn probability
- Less app engagement → higher churn
""")

# -------------------------------
# ABOUT SECTION
# -------------------------------
st.markdown("---")
st.header("📌 About Project")

st.write("""
This project predicts customer churn using machine learning.

It helps businesses:
- Identify risky customers
- Reduce churn
- Improve retention strategies
""")

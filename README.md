# customer-churn-prediction-system
End-to-end customer churn prediction system using machine learning, SQL, Power BI, and Streamlit to identify high-risk customers and drive data-driven retention strategies.
# 📊 Customer Churn Prediction & Retention Strategy System

## 🚀 Overview
This project builds an end-to-end customer churn prediction system to identify high-risk customers and enable data-driven retention strategies.

It combines:
- Machine Learning for churn prediction
- SQL for business analysis
- Power BI for visualization
- Streamlit for real-time prediction

---

## 🎯 Business Problem
Customer churn leads to revenue loss and increased acquisition cost.

This project helps businesses:
- Identify customers likely to churn
- Understand key churn drivers
- Take proactive retention actions

---

## 🧠 Key Insights
- High-risk customers show ~88% churn probability → require immediate intervention
- Customers with low tenure churn more → onboarding experience is critical
- Customers who raised complaints have significantly higher churn → service quality issue
- Higher days since last order strongly indicates disengagement

---

## ⚙️ Tech Stack
- Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)
- Machine Learning (Logistic Regression, Random Forest, XGBoost
- SQL
- Power BI
- Streamlit

---

## 📂 Project Structure
customer-churn-prediction-system/
│
├── data/ # Raw and cleaned datasets
├── notebooks/ # Jupyter notebook (EDA + Model)
├── app/ # Streamlit application
├── sql/ # SQL business queries
├── powerbi/ # Dashboard file
├── model/ # Saved model and columns
├── images/ # Dashboard screenshots
│
├── README.md
├── requirements.txt
└── .gitignore


---

## 🤖 Model Details
- Model Used: XGBoost (Calibrated)
- Target: Churn Prediction
- Output: Probability of churn

> Note: Threshold is currently set to 0.5 and can be optimized based on business cost.

---

## 💡 Business Actions
- **High Risk Customers**
  - Offer discounts
  - Personalized retention calls
  - Dedicated support

- **Medium Risk Customers**
  - Targeted marketing campaigns
  - Engagement emails/notifications

- **Low Risk Customers**
  - Loyalty programs
  - Upselling opportunities

---

## 🖥️ Dashboard Preview
![Dashboard](E:\projects\Customer churn prediction\dashboard screenshot.png)

---

## ▶️ How to Run the Project

### 1. Clone the repository
https://github.com/deveshyadav0026/customer-churn-prediction-system

### 2. Install dependencies
provided in Jupyter Notebook in first cell

### 3. Run Streamlit app
streamlit run app/app.py

## 📌 Future Improvements

- Optimize classification threshold using business cost trade-offs
- Deploy the application 
- Integrate real-time data pipelines for continuous prediction updates
- Add model explainability using SHAP for better business interpretation
- Improve model performance using hyperparameter tuning

## 👤 Author
Devesh Yadav

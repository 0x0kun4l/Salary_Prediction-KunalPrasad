# app.py

import streamlit as st
import pandas as pd
import joblib  

# Load trained model
model = joblib.load("data_analyst_sp.joblib")  


st.title("💼 Employee Salary Prediction")
st.write("Enter the job details to predict estimated average salary.")

# Input fields
analyst_type = st.selectbox("Analyst Type", ['Data Analyst', 'Business Analyst', 'Financial Analyst'])
rating = st.number_input("Company Rating (0-5)", min_value=0.0, max_value=5.0, value=3.5)
job_exp = st.selectbox("Job Experience", ['Entry Level', 'Mid Level', 'Senior Level'])
size = st.selectbox("Company Size", ['1 to 50 employees', '51 to 200 employees', '10000+ employees'])
competitors_count = st.number_input("Competitors Count", min_value=0, value=0)
company_age = st.number_input("Company Age", min_value=0, value=5)
ownership = st.selectbox("Type of Ownership", ['Private', 'Public', 'Government'])
industry = st.text_input("Industry")
sector = st.text_input("Sector")
revenue = st.selectbox("Revenue", ['Unknown', 'Less than $1 million', '$1 to $5 million', '$10+ billion'])
state = st.text_input("State")
city = st.text_input("City")

# Technologies used
SAS = st.selectbox("SAS", ['Yes', 'No'])
Hadoop = st.selectbox("Hadoop", ['Yes', 'No'])
Python = st.selectbox("Python", ['Yes', 'No'])
R_program = st.selectbox("R Programming", ['Yes', 'No'])
AWS = st.selectbox("AWS", ['Yes', 'No'])
Azure = st.selectbox("Azure", ['Yes', 'No'])
SQL = st.selectbox("SQL", ['Yes', 'No'])
Excel = st.selectbox("Excel", ['Yes', 'No'])
ML = st.selectbox("Machine Learning", ['Yes', 'No'])
Tableau = st.selectbox("Tableau", ['Yes', 'No'])
Power_BI = st.selectbox("Power BI", ['Yes', 'No'])
Qlik = st.selectbox("Qlik", ['Yes', 'No'])

if st.button("Predict Salary"):
    input_data = pd.DataFrame([{
        'Analyst_Type': analyst_type,
        'Rating': rating,
        'Job_EXP': job_exp,
        'Size': size,
        'Competitors_count': competitors_count,
        'Company_age': company_age,
        'Type_of_ownership': ownership,
        'Industry': industry,
        'Sector': sector,
        'Revenue': revenue,
        'State': state,
        'City': city,
        'SAS_extracted': SAS,
        'Hadoop_extracted': Hadoop,
        'Python_extracted': Python,
        'R_program_extracted': R_program,
        'AWS_extracted': AWS,
        'Azure_extracted': Azure,
        'SQL_extracted': SQL,
        'Excel_extracted': Excel,
        'Machine Learning_extracted': ML,
        'Tableau_extracted': Tableau,
        'Power BI_extracted': Power_BI,
        'Qlik_extracted': Qlik
    }])

    # Prediction
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Average Salary: ₹ {prediction:,.2f}")

import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('data_analyst_SP.pkl', 'rb') as file:
    model = pickle.load(file)

# App Title
st.set_page_config(page_title="Employee Salary Predictor", layout="centered")
st.title("💼 Employee Salary Prediction App")
st.markdown("Enter the details below to predict the **average salary** for an analyst role.")

# --- User Inputs ---

st.header("🔧 Basic Information")
analyst_type = st.selectbox("Analyst Type", ['Data Analyst', 'Financial Analyst', 'Business Analyst'])
rating = st.slider("Company Rating", 0.0, 5.0, 3.5, step=0.1)
job_exp = st.selectbox("Job Experience Level", ['Entry Level', 'Mid Level', 'Senior Level'])
size = st.selectbox("Company Size", ['1 to 50', '51 to 200', '201 to 500', '10000+'])

st.header("🏢 Company Details")
sector = st.selectbox("Sector", ['IT', 'Finance', 'Healthcare', 'Other'])
industry = st.text_input("Industry", "Software")
city = st.text_input("City", "San Francisco")
state = st.text_input("State", "CA")
type_of_ownership = st.selectbox("Type of Ownership", ['Private', 'Public', 'Government'])
revenue = st.selectbox("Revenue", ['Less than $1M', '$1M to $5M', '$5M to $10M', 'Unknown'])

company_age = st.number_input("Company Age (years)", min_value=0, max_value=200, value=10)
competitors_count = st.number_input("Number of Competitors", min_value=0, max_value=100, value=2)

st.header("🛠️ Technical Skills")
python = st.checkbox("Python")
excel = st.checkbox("Excel")
sql = st.checkbox("SQL")
tableau = st.checkbox("Tableau")
power_bi = st.checkbox("Power BI")
machine_learning = st.checkbox("Machine Learning")
aws = st.checkbox("AWS")
azure = st.checkbox("Azure")
sas = st.checkbox("SAS")
r_program = st.checkbox("R")
qlik = st.checkbox("Qlik")
hadoop = st.checkbox("Hadoop")

# --- Prediction ---

if st.button("🎯 Predict Salary"):
    # Build input DataFrame
    input_data = pd.DataFrame({
        'Analyst_Type': [analyst_type],
        'Rating': [rating],
        'Job_EXP': [job_exp],
        'Size': [size],
        'Sector': [sector],
        'Industry': [industry],
        'City': [city],
        'State': [state],
        'Type_of_ownership': [type_of_ownership],
        'Revenue': [revenue],
        'Company_age': [company_age],
        'Competitors_count': [competitors_count],
        'Python_extracted': [int(python)],
        'Excel_extracted': [int(excel)],
        'SQL_extracted': [int(sql)],
        'Tableau_extracted': [int(tableau)],
        'Power BI_extracted': [int(power_bi)],
        'Machine Learning_extracted': [int(machine_learning)],
        'AWS_extracted': [int(aws)],
        'Azure_extracted': [int(azure)],
        'SAS_extracted': [int(sas)],
        'R_program_extracted': [int(r_program)],
        'Qlik_extracted': [int(qlik)],
        'Hadoop_extracted': [int(hadoop)],
    })

    # Perform prediction
    try:
        prediction = model.predict(input_data)
        st.success(f"💰 Predicted Average Salary: **${prediction[0]:,.2f}**")
    except Exception as e:
        st.error(f"⚠️ Prediction failed: {str(e)}")

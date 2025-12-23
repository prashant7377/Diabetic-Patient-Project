import streamlit as st
import pandas as pd
import pickle as pkl


scaler = pkl.load(open('scaler.pkl', 'rb'))
model = pkl.load(open('model.pkl', 'rb'))
#scaler = pkl.load(open('scaler.pkl', 'rb'))


st.title("Diabetic Patient Prediction Project")

gender = st.selectbox("Select Gender", ['Female', 'Male', 'Other'])
age = st.number_input("Enter Age", min_value = 0, max_value = 100, value = 50)
hypertension = st.selectbox("Select Hypertension", ["Yes", "No"])
heart_disease = st.selectbox("Select Heart Disease", ["Yes", "No"])
smoking_history = st.selectbox("Select Smoking History", ["Naver", "No Info", "Former", "Not Current", "Ever", "Current"])
bmi = st.number_input("Enter BMI", min_value = 20, max_value = 50, value = 25)

HbA1c_level = st.number_input("Enter HbA1c level", min_value = 5.0, max_value = 10.0, value = 6.0)
blood_glucose_level = st.number_input("Enter Blood Glucose level ", min_value = 25, max_value = 500, value = 200)


if gender == 'Female':
    gender = 0
elif gender == 'Male':
    gender = 1
else:
    gender = 2


if smoking_history == 'Naver':
    smoking_history = 0
elif smoking_history == 'No Info':
    smoking_history = 1
elif smoking_history == 'Former' or smoking_history == 'Not Current':
    smoking_history = 2
elif smoking_history == 'Ever':
    smoking_history = 3
else:
    smoking_history = 4


if hypertension == 'Yes':
    hypertension = 1
else:
    hypertension = 0


if heart_disease == 'Yes':
    heart_disease = 1
else:
    heart_disease = 0

if st.button("Predict"):
    myinput = [[gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level]]
    columns = ['gender', 'age', 'hypertension', 'heart_disease', 'smoking_history', 'bmi', 'HbA1c_level', 'blood_glucose_level']
    data = pd.DataFrame(data = myinput, columns = columns)
   
    data_scaled = scaler.transform(data)
    result = model.predict(data_scaled)
    if result[0] == 1:
        st.error("Person is Diabetic.")
    else:
        st.success("Person is not Diabetic.")
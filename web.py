import os
import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

import warnings
warnings.filterwarnings("ignore",category=UserWarning)
st.set_page_config(page_title='Prediction Of Disease Outbreaks',
                   layout='wide',
                   page_icon="doctor")
diabetes_model= pickle.load(open(r"C:\Users\Lenovo\OneDrive\Documents\Disease Outbreaks\Training_models\diabetes_model.sav",'rb'))
heart_disease_model= pickle.load(open(r"C:\Users\Lenovo\OneDrive\Documents\Disease Outbreaks\Training_models\heart_model.sav",'rb'))
parkinsons_model= pickle.load(open(r"C:\Users\Lenovo\OneDrive\Documents\Disease Outbreaks\Training_models\parkinsons_model.sav",'rb'))

with st.sidebar:
    selectd= option_menu('prediction of diseas outbreak system',
                         ['Diabetes Prediction','Heart Disease Prediction','Parkinsons prediction'],
                         menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)   
    
if selectd == 'Diabetes Prediction':
    st.title('Diabetes Prediction Using Ml')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
         Bloodpressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('SkinThickness value')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the person')
diab_diagnosis =  ''
if st.button('Diabetes Test Result'):
    user_input=[Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin, 
                 BMI, DiabetesPedigreeFunction, Age ]     
    user_input= [float(x) for x in user_input]
    diab_prediction= diabetes_model.predict([user_input])
    if diab_prediction[0]== 1:
        diab_diagnosis= 'The Person is diabetic'
    else:
        diab_diagnosis= 'The Person is Not diabetic'
st.success(diab_diagnosis)

if selectd == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction Using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.text_input('Age')
    with col2:
        Sex = st.text_input('Sex')
    with col3:
        ChestPainType = st.text_input('Chest Pain Type')
    with col1:
        RestingBP = st.text_input('Resting Blood Pressure')
    with col2:
        Cholesterol = st.text_input('Serum Cholesterol')
    with col3:
        FastingBS = st.text_input('Fasting Blood Sugar')
    with col1:
        RestingECG = st.text_input('Resting ECG')
    with col2:
        MaxHR = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        ExerciseAngina = st.text_input('Exercise-Induced Angina')
    
    if st.button('Heart Disease Test Result'):
        user_input = [float(x) for x in [Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina]]
        heart_prediction = heart_disease_model.predict([user_input])
        
        # Now define the result variable here:
        if heart_prediction[0] == 1:
            result = 'The person has heart disease'
        else:
            result = 'The person does not have heart disease'
        
        st.success(result)

if selectd == 'Parkinsons prediction':
    st.title('Parkinson\'s Disease Prediction Using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        FoM = st.text_input('Motor Activity (FoM)')
    with col2:
        MDVP_FoH = st.text_input('Average Fundamental Frequency')
    with col3:
        MDVP_Fhi = st.text_input('Highest Frequency')
    with col1:
        MDVP_Flo = st.text_input('Lowest Frequency')
    with col2:
        MDVP_Jitter = st.text_input('Jitter')
    with col3:
        MDVP_Shimmer = st.text_input('Shimmer')
    with col1:
        MDVP_APQ = st.text_input('Shimmer in 3-5 segments')
    with col2:
        MDVP_APQ3 = st.text_input('Shimmer in 6-10 segments')
    with col3:
        NHR = st.text_input('Noise to Harmonics Ratio')
    with col1:
        HNR = st.text_input('Harmonics to Noise Ratio')
    with col2:
        RPDE = st.text_input('Recurrence Period Density Entropy')
    with col3:
        D2 = st.text_input('Determinism in signal')
    
    # Initialize parkinsons_diagnosis variable here
    parkinsons_diagnosis = ''
    
    if st.button('Parkinson\'s Test Result'):
        user_input = [
            float(FoM), float(MDVP_FoH), float(MDVP_Fhi), float(MDVP_Flo), 
            float(MDVP_Jitter), float(MDVP_Shimmer), float(MDVP_APQ), 
            float(MDVP_APQ3), float(NHR), float(HNR), float(RPDE), float(D2)
        ]
        parkinson_prediction = parkinsons_model.predict([user_input])
        if parkinson_prediction[0] == 1:
            parkinsons_diagnosis = 'The person has Parkinson\'s disease'
        else:
            parkinsons_diagnosis = 'The person does not have Parkinson\'s disease'
        
    # Display the result only after button is pressed
    if parkinsons_diagnosis:
        st.success(parkinsons_diagnosis)


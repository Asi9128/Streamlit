import streamlit as st
import pickle
import pandas as pd
from pathlib import Path
import os
# load the pipeline
# @st.cache_resource
# def load_pipeline():
    #with open(os.path.join('Models', 'premodel.pkl'), 'rb') as file:
    # with (open('Models')/'premodel.pkl', 'rb') as file:
      # return pickle.load(file)
@st.cache_resource
def load_pipeline():
    pipeline_path = Path('Models') / 'premodel.pkl'
    with open(pipeline_path, 'rb') as file:
        return pickle.load(file)
    
def load_model(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

def predict_page():

    st.sidebar.title("Predict Page")
    st.sidebar.write("Churn or not Churn Prediction")


    #load pipeline
    pipeline = load_pipeline()

    #load models
    models_path = {
        'Decision Tree':'Models/Decision Tree.pkl',
        'K-Nearest Neigbors':'Models/K-Nearest Neighbors.pkl',
        'XGB':'Models/XGB.pkl'
    }

    model_choice = st.selectbox('Select a Model', list(models_path.keys()))
    model = load_model(models_path[model_choice])

    if model is None:
        st.error('Model is not selected')
        return

    #check the model type
    st.write(f"Loaded Model Type: {type(model)}")

    #make single prediction
    st.subheader("Single Customer Prediction")
    
    gender = st.selectbox("gender", ['Male', 'Female'])
    SeniorCitizen = st.selectbox("Senior Citizen", ['Yes', 'No'])
    Partner = st.selectbox("Partner", ['Yes', 'No'])
    Dependents = st.selectbox("Dependents", ['Yes', 'No'])
    tenure = st.slider("tenure (Months)", min_value=1, max_value=72, value=12)
    PaperlessBilling = st.selectbox("Paperless Billing", ['Yes', 'No'])
    PaymentMethod = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
    MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
    TotalCharges = st.number_input("Total Charges", min_value=0.0, value=500.0)
    PhoneService = st.selectbox("Phone Service", ['Yes', 'No'])
    MultipleLines = st.selectbox("Multiple Lines", ['Yes', 'No', 'No phone service'])
    InternetService = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
    OnlineSecurity = st.selectbox("Online Security", ['Yes', 'No', 'No internet service'])
    OnlineBackup = st.selectbox("Online Backup", ['Yes', 'No', 'No internet service'])
    DeviceProtection = st.selectbox("Device Protection", ['Yes', 'No', 'No internet service'])
    TechSupport = st.selectbox("Tech Support", ['Yes', 'No', 'No internet service'])
    StreamingTV = st.selectbox("StreamingTV", ['Yes', 'No', 'No internet service'])
    StreamingMovies = st.selectbox("StreamingMovies", ['Yes', 'No', 'No internet service'])
    Contract = st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])
    Churn = st.selectbox("Churn", ['Yes', 'No'])
   
    #predict for a customer
    if st.button('Predict'):

        #create a dataframe
        data = pd.DataFrame({
            'gender': [gender],
            'SeniorCitizen': [SeniorCitizen],
            'Partner': [Partner],
            'Dependents': [Dependents],
            'tenure': [tenure],
            'PaperlessBilling': [PaperlessBilling],
            'PaymentMethod': [PaymentMethod],
            'MonthlyCharges': [MonthlyCharges],
            'TotalCharges': [TotalCharges],
            'PhoneService': [PhoneService],
            'MultipleLines': [MultipleLines],
            'InternetService': [InternetService],
            'OnlineSecurity': [OnlineSecurity],
            'OnlineBackup': [OnlineBackup],
            'DeviceProtection': [DeviceProtection],
            'TechSupport': [TechSupport],
            'StreamingTV': [StreamingTV],
            'StreamingMovies': [StreamingMovies],
            'Contract': [Contract],
            'Churn': [Churn]
        })

        #Process to the pipeline
        predition = pipeline.predict(data)
        probability = pipeline.predict_proba(data)[0][1]*100

        #Display results
        st.write(f"Single Prediction:{'Churn' if predition[0] == 1 else 'Not Churn'}")
        st.write(f"Churn Probability:{probability:.2f}%")
    
    #Bulk Prediction
    st.header("Bulk Customer Prediction")
    st.write("Upload CSV File")
    uploaded_file = st.file_uploader("Upload CSV File", type="csv")

    if uploaded_file is not None:
        try:
            #read the data
            bulk_data = pd.read_csv(uploaded_file)
            st.write("Data Preview",bulk_data.head())
        
            #required columns
            required_columns = [
                'Gender','SeniorCitizen','Partner','Dependents','Tenure','PhoneService',
                'MultipleLines','InternetService','OnlineSecurity','OnlineBackup',
                'DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract',
                'PaperlessBilling','PaymentMethod','MonthlyCharges','TotalCharges','Churn'
            ]
    
            if all(col in bulk_data.columns for col in required_columns):
       
                bulk_predictions = pipeline.predict(bulk_data)
                bulk_probabilities = pipeline.predict_proba(bulk_data)[:,1]*100

                #Display results    
                bulk_results = bulk_data.copy()
                bulk_results["Predictions"] = ['Churn' if pred == 1 else 'Not Churn' for pred in bulk_predictions]
                bulk_results["Churn Probability"] = bulk_probabilities

                st.write("Bulk Prediction Results:")
                st.dataframe(bulk_results)


                 #save the results to a CSV file
                result_file = "data/bulk_predictions.csv"
                bulk_results.to_csv(result_file, index=False)
                st.success(f"Results saved to {result_file}")
        
            else:
                st.error("Upload CSV file with required columns")

    
        except Exception as e:
            st.error(f"Error during bulk prediction: {e}")
                 

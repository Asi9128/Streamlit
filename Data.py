import streamlit as st
import pandas as pd

def data_page():

    st.title("Data Page 📈")

    st.sidebar.title("Data Understanding")
    
    st.sidebar.write("This provide insights about the data")

    columns_description = {
        "Gender": "Whether the customer is a male or a female",
        "SeniorCitizen": "Whether a customer is a senior citizen or not",
        "Partner": "Whether the customer has a partner or not (Yes, No)",
        "Dependents": "Whether the customer has dependents or not (Yes, No)",
        "Tenure": "Number of months the customer has stayed with the company",
        "PhoneService": "Whether the customer has a phone service or not (Yes, No)",
        "MultipleLines": "Whether the customer has multiple lines or not",
        "InternetService": "Customer's internet service provider (DSL, Fiber Optic, No)",
        "OnlineSecurity": "Whether the customer has online security or not (Yes, No, No Internet)",
        "OnlineBackup": "Whether the customer has online backup or not (Yes, No, No Internet)",
        "DeviceProtection": "Whether the customer has device protection or not (Yes, No, No Internet)",
        "TechSupport": "Whether the customer has tech support or not (Yes, No, No Internet)",
        "StreamingTV": "Whether the customer has streaming TV or not (Yes, No, No Internet)",
        "StreamingMovies": "Whether the customer has streaming movies or not (Yes, No, No Internet)",
        "Contract": "The contract term of the customer (Month-to-Month, One year, Two year)",
        "PaperlessBilling": "Whether the customer has paperless billing or not (Yes, No)",
        "Payment Method": "The customer's payment method (Electronic check, mailed check, Bank transfer(automatic), Credit card(automatic))",
        "MonthlyCharges": "The amount charged to the customer monthly",
        "TotalCharges": "The total amount charged to the customer",
        "Churn": "Whether the customer churned or not (Yes or No)"
    }
    

    # creating columns
    col1, col2 = st.columns(2)

    with col1:
        selected_column = st.selectbox(
            "## Data Description", 
            list(columns_description.keys()),
            key ="columns_description_select"
        )
        st.write(columns_description[selected_column])

    with col2:
        def filter_column(data):
            data_type = st.selectbox(
                "Select Data Type",
                ["All","Numeric", "Categorical"]
            )
            
            if data_type == "Numeric":
                data = data.select_dtypes(include=["number"])
            elif data_type == "Categorical":
                data = data.select_dtypes(include=["object", "category"])

            st.write("## Filtered Data Preview")
            st.write(data)


        # loading dataset
        dataset_path = r"C:\Users\HP1\Desktop\Streamlit\Data\train_copy1.csv"
        try:
            data = pd.read_csv(dataset_path)
            with col2:
                filter_column(data)
        except FileNotFoundError:
            st.error("Dataset not found at {dataset_path}. Please upload a dataset.")
        except Exception as e:
            st.error(f"An error occurred while loading the dataset: {str(e)}")
        
        # data = pd.read_csv(dataset_path)
        # filter_column(data)


# import streamlit as st
# import pandas as pd

# # def data_page():
#     st.title("Data Page")
#     st.sidebar.title("Data Understanding")
#     st.sidebar.write("This section provides insights about the data.")

#     columns_description = {
#         "Gender": "Whether the customer is a male or a female",
#         "SeniorCitizen": "Whether a customer is a senior citizen or not",
#         "Partner": "Whether the customer has a partner or not (Yes, No)",
#         "Dependents": "Whether the customer has dependents or not (Yes, No)",
#         "Tenure": "Number of months the customer has stayed with the company",
#         "Phone Service": "Whether the customer has a phone service or not (Yes, No)",
#         "MultipleLines": "Whether the customer has multiple lines or not",
#         "InternetService": "Customer's internet service provider (DSL, Fiber Optic, No)",
#         "OnlineSecurity": "Whether the customer has online security or not (Yes, No, No Internet)",
#         "OnlineBackup": "Whether the customer has online backup or not (Yes, No, No Internet)",
#         "DeviceProtection": "Whether the customer has device protection or not (Yes, No, No Internet)",
#         "TechSupport": "Whether the customer has tech support or not (Yes, No, No Internet)",
#         "StreamingTV": "Whether the customer has streaming TV or not (Yes, No, No Internet)",
#         "StreamingMovies": "Whether the customer has streaming movies or not (Yes, No, No Internet)",
#         "Contract": "The contract term of the customer (Month-to-Month, One year, Two year)",
#         "PaperlessBilling": "Whether the customer has paperless billing or not (Yes, No)",
#         "Payment Method": "The customer's payment method (Electronic check, mailed check, Bank transfer(automatic), Credit card(automatic))",
#         "MonthlyCharges": "The amount charged to the customer monthly",
#         "TotalCharges": "The total amount charged to the customer",
#         "Churn": "Whether the customer churned or not (Yes or No)"
#     }

#     # Creating columns
#     col1, col2 = st.columns(2)

#     # Display column description in col1
#     with col1:
#         selected_column = st.selectbox(
#             "Data Description", 
#             list(columns_description.keys()),
#             key="columns_description_select"
#         )
#         st.write(columns_description[selected_column])

#     # Load and filter dataset in col2
#     dataset_path = r"C:\Users\HP1\Desktop\Streamlit\Data\train_copy.csv"
#     try:
#         data = pd.read_csv(dataset_path)

#         with col2:
#             st.write("## Filtered Data Preview")
#             data_type = st.selectbox(
#                 "Select Data Type",
#                 ["All", "Numeric", "Categorical"]
#             )
            
#             if data_type == "Numeric":
#                 filtered_data = data.select_dtypes(include=["number"])
#             elif data_type == "Categorical":
#                 filtered_data = data.select_dtypes(include=["object", "category"])
#             else:
#                 filtered_data = data

#             st.write(filtered_data.head())
#     except FileNotFoundError:
#         st.error(f"Dataset not found at {dataset_path}. Please upload a dataset.")
#     except Exception as e:
#         st.error(f"An error occurred while loading the dataset: {str(e)}")

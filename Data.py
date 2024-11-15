# import streamlit as st
# import pandas as pd

# def data_page():

#     st.title("Data Page 📈")

#     st.sidebar.title("Data Understanding")
    
#     st.sidebar.write("This provide insights about the data")

#     columns_description = {
#         "Gender": "Whether the customer is a male or a female",
#         "SeniorCitizen": "Whether a customer is a senior citizen or not",
#         "Partner": "Whether the customer has a partner or not (Yes, No)",
#         "Dependents": "Whether the customer has dependents or not (Yes, No)",
#         "Tenure": "Number of months the customer has stayed with the company",
#         "PhoneService": "Whether the customer has a phone service or not (Yes, No)",
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
    

#     # creating columns
#     col1, col2 = st.columns(2)

#     with col1:
#         selected_column = st.selectbox(
#             "## Data Description", 
#             list(columns_description.keys()),
#             key ="columns_description_select"
#         )
#         st.write(columns_description[selected_column])

#     with col2:
#         def filter_column(data):
#             data_type = st.selectbox(
#                 "Select Data Type",
#                 ["All","Numeric", "Categorical"]
#             )
            
#             if data_type == "Numeric":
#                 data = data.select_dtypes(include=["number"])
#             elif data_type == "Categorical":
#                 data = data.select_dtypes(include=["object", "category"])

#             st.write("## Filtered Data Preview")
#             st.write(data)


#         # loading dataset
#         dataset_path = r"C:\Users\HP1\Desktop\Streamlit\Data\train_copy1.csv"
#         try:
#             data = pd.read_csv(dataset_path)
#             with col2:
#                 filter_column(data)
#         except FileNotFoundError:
#             st.error("Dataset not found at {dataset_path}. Please upload a dataset.")
#         except Exception as e:
#             st.error(f"An error occurred while loading the dataset: {str(e)}")
        

import streamlit as st
import pandas as pd

# Load data
file_path = r"C:\Users\HP1\Desktop\Streamlit\Data\train_copy1.csv"
print(file_path)
data = pd.read_csv(file_path)

# Define the data page function
def data_page():
    # Set up custom styles
    st.markdown(
        """
        <style>
        .main-title {
            font-size: 36px;
            color: #4a4a4a;
            text-align: center;
            font-weight: bold;
            margin-top: 0;
        }
        .section-title {
            font-size: 24px;
            color: #6b6b6b;
            font-weight: bold;
            margin-top: 40px;
        }
        .dataframe {
            background-color: #f8f9fa;
            border: 1px solid #e0e0e0;
            border-radius: 5px;
            padding: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Title for the data page
    st.markdown("<div class='main-title'>Customer Churn Data Overview</div>", unsafe_allow_html=True)

    # Sidebar filters
    st.sidebar.title("Data Filters")
    gender_filter = st.sidebar.multiselect("Gender", options=data["gender"].unique(), default=data["gender"].unique())
    internet_service_filter = st.sidebar.multiselect("Internet Service", options=data["InternetService"].unique(), default=data["InternetService"].unique())
    contract_filter = st.sidebar.multiselect("Contract Type", options=data["Contract"].unique(), default=data["Contract"].unique())

    # Filter data based on sidebar selections
    filtered_data = data[
        (data["gender"].isin(gender_filter)) &
        (data["InternetService"].isin(internet_service_filter)) &
        (data["Contract"].isin(contract_filter))
    ]

    # Display data overview section
    st.markdown("<div class='section-title'>Filtered Data Summary</div>", unsafe_allow_html=True)
    st.write("Showing a summary of the data based on your selected filters.")
    st.write(filtered_data.describe())

    # Display full filtered data
    st.markdown("<div class='section-title'>Full Filtered Data</div>", unsafe_allow_html=True)
    st.write("You can scroll through the filtered data below.")
    st.write(filtered_data.style.set_properties(**{'background-color': '#f5f5f5', 'color': '#333', 'border-color': 'black'}))

    # Download button
    st.markdown("<div class='section-title'>Download Filtered Data</div>", unsafe_allow_html=True)
    csv = filtered_data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name='filtered_data.csv',
        mime='text/csv',
        help="Download the filtered dataset as a CSV file",
    )

# Add a call to this function in your main app file to display this page

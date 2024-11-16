import streamlit as st
import pandas as pd
import os

print("Current Working Directory: ", os.getcwd())
file_path = os.path.join(os.getcwd(), "Data", "train_copy1.csv")
data = pd.read_csv(file_path)


# Data page function
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


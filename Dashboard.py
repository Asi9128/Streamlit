# import streamlit as st
# import pandas as pd 
# import matplotlib.pyplot as plt
# import seaborn as sns 


# def dashboard_page():

#     st.title("Dashboard Page")

#     #load data
#     try:
#         data = pd.read_csv("data/train_copy.csv")
#     except FileNotFoundError:
#         st.error("Dataset not found at {dataset_path}. Please upload a dataset.")
#         return


#     st.header("Data Overview")
#     st.write("Summary of the dataset")
#     st.dataframe(data.head())

#     st.subheader("Churn Count")
#     churn_count = (data["Churn"].value_counts())
#     st.bar_chart(churn_count)

#     # Plot Correlation Matrix
#     st.subheader("Correlation Matrix")
#     numeric_columns = data.select_dtypes(include=["number"])

#     corr = data.corr(["tenure","MonthlyCharges","TotalCharges"])

#     plt.figure(figsize=(10,10))
#     sns.heatmap(corr, annot=True,cmap="coolwarm",fmt=".2f")
#     st.pyplot(plt) 



# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# def dashboard_page():
#     st.title("Dashboard Page")

#     # Load data
#     data = pd.read_csv("data/train_copy.csv")

#     st.header("Data Overview")
#     st.write("Summary of the dataset")
#     st.dataframe(data.head())

#     st.subheader("Churn Count")
#     churn_count = data["Churn"].value_counts()
#     st.bar_chart(churn_count)

#     # Filter numeric columns for the correlation matrix
#     st.subheader("Correlation Matrix")
#     numeric_columns = data.select_dtypes(include=["number"])

#     # Check if the specified columns are in the dataset
#     columns_to_correlate = ["Tenure", "MonthlyCharges", "TotalCharges"]
#     available_columns = [col for col in columns_to_correlate if col in numeric_columns.columns]
    
#     # Calculate and display the correlation matrix if the columns are available
#     if available_columns:
#         corr = numeric_columns[available_columns].corr()
#         plt.figure(figsize=(10, 10))
#         sns.heatmap(corr, annot=True, cmap="coolwarm")
#         st.pyplot(plt)
#     else:
#         st.error("The specified columns for correlation are not available in the dataset.")


#     #  Plot bar chart
#     st.checkbox("Show Churn Count"):
#     st.subheader("Churn Count")
#     churn_count = data["Churn"].value_counts()
#     st.bar_chart(churn_count)

#     # Plot pie chart
#     st.subheader("Churn Ratio")
#     churn_ratio = data["Churn"].value_counts(normalize=True) * 100
#     st.pie_chart(churn_ratio)

#     # Plot line chart
#     st.subheader("Churn Over Time")
#     churn_over_time = data.groupby("")["Churn"].value_counts(normalize=True) * 100
#     st.line_chart(churn_over_time)





# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
 
 
# def dashboard_page():
#     st.title('Dashboard Page 📊')
 
#     # load data
#     data = pd.read_csv(r"C:\Users\HP1\Desktop\Streamlit\Data\train_copy1.csv")
 
#     st.header('Data Overview')
#     st.write('Here is a quick summary of the data')
#     st.dataframe(data.head())
 
#     st.subheader('Churn Count')
#     churn_count = data['Churn'].value_counts()
#     st.bar_chart(data=churn_count)
 
#     # Churn Rate Pie Chart
#     st.subheader("Churn Rate")
#     churn_counts = data['Churn'].value_counts()
#     fig, ax = plt.subplots()
#     ax.pie(churn_counts, labels=['No Churn', 'Churn'], autopct='%1.1f%%', startangle=90)
#     st.pyplot(fig)
 
#     # Tenure and Churn Histogram
#     st.subheader("Tenure Distribution by Churn Status")
#     fig, ax = plt.subplots()
#     sns.histplot(data=data, x="tenure", hue="Churn", multiple="stack", ax=ax)
#     st.pyplot(fig)
 
#     # Monthly Charges Box Plot
#     st.subheader("Monthly Charges by Churn Status")
#     fig, ax = plt.subplots()
#     sns.boxplot(data=data, x="Churn", y="MonthlyCharges", ax=ax)
#     st.pyplot(fig)
 
#     # Contract Type vs Churn Rate
#     st.subheader("Churn Rate by Contract Type")
#     contract_churn = pd.crosstab(data['Contract'], data['Churn'], normalize='index')  # Normalize by row for percentage
#     contract_churn = contract_churn.rename({0: 'Not Churned', 1: 'Churned'}, axis=1)
#     fig, ax = plt.subplots()
#     contract_churn.plot(kind='bar', stacked=True, ax=ax, color=['green', 'red'])
#     ax.set_ylabel('Churn Rate')
#     ax.set_title('Churn Rate by Contract Type')
#     st.pyplot(fig)
 
#      # Payment Method vs Churn
#     st.subheader("Churn Rate by Payment Method")
#     payment_churn = pd.crosstab(data['PaymentMethod'], data['Churn'], normalize='index')  # Normalize by row for percentage
#     payment_churn = payment_churn.rename({0: 'Not Churned', 1: 'Churned'}, axis=1)
#     fig, ax = plt.subplots()
#     payment_churn.plot(kind='bar', stacked=True, ax=ax, color=['green', 'red'])
#     ax.set_ylabel('Churn Rate')
#     ax.set_title('Churn Rate by Payment Method')
#     st.pyplot(fig)
 
#     # Internet Service vs Churn
#     st.subheader("Churn Rate by Internet Service")
#     internet_churn = pd.crosstab(data['InternetService'], data['Churn'], normalize='index')  # Normalize by row for percentage
#     internet_churn = internet_churn.rename({0: 'Not Churned', 1: 'Churned'}, axis=1)
#     fig, ax = plt.subplots()
#     internet_churn.plot(kind='bar', stacked=True, ax=ax, color=['green', 'red'])
#     ax.set_ylabel('Churn Rate')
#     ax.set_title('Churn Rate by Internet Service')
#     st.pyplot(fig)





# Dashboard.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
file_path = (r"C:\Users\HP1\Desktop\Streamlit\Data\train_copy1.csv")
data = pd.read_csv(file_path)

# Define the dashboard_page function
def dashboard_page():
    # Set up the Streamlit app layout
    st.title("Customer Churn Dashboard")
    st.sidebar.title("Filters")

    # Sidebar filters
    gender_filter = st.sidebar.multiselect("Gender", options=data["gender"].unique(), default=data["gender"].unique())
    internet_service_filter = st.sidebar.multiselect("Internet Service", options=data["InternetService"].unique(), default=data["InternetService"].unique())
    contract_filter = st.sidebar.multiselect("Contract Type", options=data["Contract"].unique(), default=data["Contract"].unique())
    payment_method_filter = st.sidebar.multiselect("Payment Method", options=data["PaymentMethod"].unique(), default=data["PaymentMethod"].unique())

    # Filter data based on selections
    filtered_data = data[
        (data["gender"].isin(gender_filter)) &
        (data["InternetService"].isin(internet_service_filter)) &
        (data["Contract"].isin(contract_filter)) &
        (data["PaymentMethod"].isin(payment_method_filter))
    ]

    # Display a summary of filtered data
    st.write("### Summary of Filtered Data")
    st.write(filtered_data.describe())

    # Churn distribution
    st.write("### Churn Distribution")
    churn_counts = filtered_data["Churn"].value_counts()
    fig, ax = plt.subplots(facecolor="#f2e6ff")
    ax.pie(churn_counts, labels=churn_counts.index, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    colors = ["#ff9999", "#66b3ff"]
    ax.pie(churn_counts, labels=churn_counts.index, colors=colors, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")

    st.pyplot(fig)

    # Monthly Charges Distribution
    st.write("### Monthly Charges Distribution")
    fig, ax = plt.subplots(facecolor="#ffebcc")
    sns.histplot(filtered_data["MonthlyCharges"], bins=30, kde=True, ax=ax)
    st.pyplot(fig)

    # Total Charges vs. Tenure
    st.write("### Total Charges vs. Tenure")
    fig, ax = plt.subplots(facecolor="#e6f7ff")
    sns.scatterplot(data=filtered_data, x="tenure", y="TotalCharges", hue="Churn", ax=ax)
    st.pyplot(fig)

    # Service Subscription Counts
    st.write("### Service Subscription Counts")
    services = ["PhoneService", "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies"]
    service_counts = filtered_data[services].apply(pd.Series.value_counts)
    st.write(service_counts)

    # Contract Type vs Churn Rate
    st.write("### Churn Rate by Contract Type")
    contract_churn = pd.crosstab(filtered_data['Contract'], filtered_data['Churn'], normalize='index')  # Normalize by row for percentage
    contract_churn = contract_churn.rename({0: 'Not Churned', 1: 'Churned'}, axis=1)
    fig, ax = plt.subplots(facecolor="#f5f5f5")
    contract_churn.plot(kind='barh', stacked=True, ax=ax, color=['black', 'red'])
    ax.set_ylabel('Churn Rate')
    ax.set_title('Churn Rate by Contract Type')
    st.pyplot(fig)

    # Payment Method vs Churn
    st.write("### Churn Rate by Payment Method")
    payment_churn = pd.crosstab(filtered_data['PaymentMethod'], filtered_data['Churn'], normalize='index')  # Normalize by row for percentage
    payment_churn = payment_churn.rename({0: 'Not Churned', 1: 'Churned'}, axis=1)
    fig, ax = plt.subplots(facecolor="#e6f7ff")
    payment_churn.plot(kind='bar', stacked=True, ax=ax, color=['blue', 'pink'])
    ax.set_ylabel('Churn Rate')
    ax.set_title('Churn Rate by Payment Method')
    st.pyplot(fig)

    # Internet Service vs Churn
    st.write("### Churn Rate by Internet Service")
    internet_churn = pd.crosstab(filtered_data['InternetService'], filtered_data['Churn'], normalize='index')  # Normalize by row for percentage
    internet_churn = internet_churn.rename({0: 'Not Churned', 1: 'Churned'}, axis=1)
    fig, ax = plt.subplots(facecolor="#f2e6ff")
    internet_churn.plot(kind='bar', stacked=True, ax=ax, color=['lightgreen', 'lightblue'])
    ax.set_ylabel('Churn Rate')
    ax.set_title('Churn Rate by Internet Service')
    st.pyplot(fig)

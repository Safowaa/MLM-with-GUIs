import streamlit as st
import pandas as pd
import yaml
import matplotlib.pyplot as plt
import io
import pyodbc
import os

def data_page():
    # Set the logo and title
    col1, col2 = st.columns([1, 10])  # Adjust the width ratio to balance logo and title
    with col1:
        st.image("logo/Logo.png", width=100)
        
    with col2:
        st.markdown("<h1 style='font-size: 58px;'>Japan Machine Training Ltd</h1>", unsafe_allow_html=True)

    st.write(" ## Data Used for Training and Testing")
    st.write("""
             ### The dataset used in this project contains various attributes of customers, including:
- CustomerID
- Gender
- SeniorCitizen
- Partner
- Dependents
- Tenure
- PhoneService
- MultipleLines
- InternetService
- OnlineSecurity
- OnlineBackup
- DeviceProtection
- TechSupport
- StreamingTV
- StreamingMovies
- Contract
- PaperlessBilling
- PaymentMethod
- MonthlyCharges
- TotalCharges
- Churn 

#### Note: The Test data does not have the churn column
     """)
    
    st.write(""" 
             For each column there were unique values, the following columns had boolen features Yes/No only. 
             Senior Citizen, Partner, Dependents, Phone Service, Multiple Lines, Online Security, Online Backup, Device Protection, Tech Support, Streaming TV, Streaming Movies, and Paperless Billing.
             The numeric columns are; Tenure (Months), Monthly Charges, and Total Charges.
             Other columns like Gender has Male and Female, Internet Service has DSL, Fiber Optic and No, Contract has Month-to-Month, One year, and Two year, Payment Method has Electronic check, Mailed check, and Bank transfer. 
             """)
    
    # Load the configuration from YAML file
    with open(r'config\config.yaml', 'r') as file:
        config = yaml.safe_load(file)


    # Database connection parameters from .env file
    SERVER = config["SERVER"]
    DATABASE = config["DATABASE"]
    USERNAME = config["USERNAME"]
    PASSWORD = config["PASSWORD"]
    DRIVER = config["DRIVER"]

    # Path to the additional CSV file from .env file
    CSV_PATH = (r"data_files\LP2_Telco-churn-second-2000.csv")
    CSV_PATH1 = (r"data_files\Telco-churn-last-2000.xlsx")
    CSV_PATH2 = (r"data_files\train_data.csv")
    CSV_PATH3 = (r"data_files\test_data_with_predictions.csv")


    # Function to load data from the database
    def load_data():
        conn_str = f"DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}"
        conn = pyodbc.connect(conn_str)
        query = "SELECT * FROM dbo.LP2_Telco_churn_first_3000"
        data = pd.read_sql(query, conn)
        conn.close()
        return data

    # Function to load additional CSV files
    def load_additional_csv(path):
        return pd.read_csv(path)

    def load_additional_xlsx(path):
        return pd.read_excel(path)

    # Function to create a plot of the data
    def create_plot(data):
        fig, ax = plt.subplots(figsize=(10, 6))
        data.head(50).plot(ax=ax)
        plt.title('Data Plot')
        plt.xlabel('Index')
        plt.ylabel('Values')
        plt.grid(True)
        plt.tight_layout()
        return fig

    # Function to convert plot to image and provide download link
    def plot_to_image(fig):
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        return buf

    # Load and display data from the database
    data = load_data()
    st.subheader("First 50 Rows Of Part Of The Data Used to Train The Models ")
    st.dataframe(data.head(50))

    # Provide CSV download link
    st.subheader("Download Data File")
    csv = data.to_csv(index=False)
    st.download_button(
        label="Download",
        data=csv,
        file_name='data.csv',
        mime='text/csv'
    )

    # Create and provide image download link
    st.subheader("Download Data Image")
    fig = create_plot(data)
    buf = plot_to_image(fig)
    st.download_button(
        label="Download",
        data=buf,
        file_name='data_plot.png',
        mime='image/png'
    )

    # Load and display additional CSV data
    additional_data = load_additional_csv(CSV_PATH)
    st.subheader("Other Half Of The Data Used To Train The Models")
    st.dataframe(additional_data.head(50))

    # Provide download options for additional CSV data
    st.subheader("Download Data File")
    csv_additional = additional_data.to_csv(index=False)
    st.download_button(
        label="Download",
        data=csv_additional,
        file_name='additional_data.csv',
        mime='text/csv'
    )

    # Create and provide plot download link for additional CSV data
    st.subheader("Download Data Image")
    fig_additional = create_plot(additional_data)
    buf_additional = plot_to_image(fig_additional)
    st.download_button(
        label="Download",
        data=buf_additional,
        file_name='additional_data_plot.png',
        mime='image/png'
    )

# Load and display merged data from an Excel file
    merged_data = load_additional_xlsx(CSV_PATH1)
    st.subheader("A Display Of The Data Used to Train the models Merged")
    st.dataframe(merged_data.head(50))

    # Provide download options for merged data
    st.subheader("Download File")
    xlsx_buf = io.BytesIO()
    with pd.ExcelWriter(xlsx_buf, engine='xlsxwriter') as writer:
        merged_data.to_excel(writer, index=False)
        writer.close()
        xlsx_buf.seek(0)

    st.download_button(
        label="Download",
        data=xlsx_buf,
        file_name='merged_data.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    # Create and provide plot download link for merged data
    st.subheader("Download Data Image")
    fig_merged = create_plot(merged_data)
    buf_merged = plot_to_image(fig_merged)
    st.download_button(
        label="Download Image",
        data=buf_merged,
        file_name='merged_data_plot.png',
        mime='image/png'
    )

    # Load and display test data
    test_data = load_additional_csv(CSV_PATH2)
    st.subheader("A Display Of The Test Data")
    st.dataframe(test_data.head(50))

    # Provide download options for test data
    st.subheader("Download File")
    csv_test = test_data.to_csv(index=False)
    st.download_button(
        label="Download",
        data=csv_test,
        file_name='test_data.csv',
        mime='text/csv'
    )

    # Create and provide plot download link for test data
    st.subheader("Download Test Data Image")
    fig_test = create_plot(test_data)
    buf_test = plot_to_image(fig_test)
    st.download_button(
        label="Download Image",
        data=buf_test,
        file_name='test_data_plot.png',
        mime='image/png'
    )
    
    # Load and display test data with predicted column
    predict_data = load_additional_csv(CSV_PATH3)
    st.subheader("""A Display Of The Data Used in Testing the Machine Learning Modules with the predicted values using Logistic Regression""")
    st.dataframe(predict_data.head(50))

    # Provide download options for test data with predicted column
    st.subheader("Download CSV File with churn colum")
    csv_pred = predict_data.to_csv(index=False)
    st.download_button(
        label="Download",
        data=csv_pred,
        file_name='test_data.csv',
        mime='text/csv'
    )

    # Create and provide plot download link for test datawith predicted column
    st.subheader("Download Test Data Image with churn colum")
    fig_test = create_plot(test_data)
    buf_test = plot_to_image(fig_test)
    st.download_button(
        label="Download",
        data=buf_test,
        file_name='test_data_plot.png',
        mime='image/png'
    )


    st.write("---")
    # Add copyright notice
    st.write("© 2024 Japan Machine Training Ltd. All Rights Reserved.")

# Call the data_page function when the module is run
if __name__ == "__main__":
    data_page()

import streamlit as st
import pandas as pd
import yaml
import matplotlib.pyplot as plt
import io
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import os

# Function to load a file from S3
def load_file_from_s3(file_key, is_yaml=False):
    bucket_name = os.getenv("AWS_BUCKET_NAME")
    
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION"),
    )

    try:
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        file_content = response['Body'].read()

        if is_yaml:
            return yaml.safe_load(file_content)
        else:
            return io.BytesIO(file_content)  # Return as a file-like object for non-YAML files

    except s3.exceptions.NoSuchKey:
        st.error(f"File {file_key} not found in S3.")
        return None
    except (NoCredentialsError, ClientError) as e:
        st.error(f"Error downloading {file_key} from S3: {str(e)}")
        return None

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

def data_page():
    # Set the logo and title
    col1, col2 = st.columns([1, 10])  # Adjust the width ratio to balance logo and title
    with col1:
        st.image("logo/Logo.png", width=100)
        
    with col2:
        st.markdown("<h1 style='font-size: 58px;'>Japan Machine Training Ltd</h1>", unsafe_allow_html=True)

    st.write(" ## Data Used for Training and Testing")
    
    # Load the configuration from YAML file in S3
    config = load_file_from_s3("config.yaml", is_yaml=True)
    if config is None:
        st.stop()  # Stop if config is not loaded

    SERVER = config["SERVER"]
    DATABASE = config["DATABASE"]
    USERNAME = config["USERNAME"]
    PASSWORD = config["PASSWORD"]
    DRIVER = config["DRIVER"]

    # File paths from S3
    csv_file_key1 = "data_files/LP2_Telco-churn-second-2000.csv"
    csv_file_key2 = "data_files/Telco-churn-last-2000.xlsx"
    csv_file_key3 = "data_files/train_data.csv"
    csv_file_key4 = "data_files/test_data_with_predictions.csv"

    # Function to load CSV or Excel from S3
    def load_csv_from_s3(file_key):
        file_data = load_file_from_s3(file_key)
        if file_data is not None:
            return pd.read_csv(file_data)
        else:
            return None

    def load_excel_from_s3(file_key):
        file_data = load_file_from_s3(file_key)
        if file_data is not None:
            return pd.read_excel(file_data)
        else:
            return None

    # Load and display the first part of the data
    data = load_csv_from_s3(csv_file_key1)
    if data is not None:
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

    # Load and display additional data (Excel)
    additional_data = load_excel_from_s3(csv_file_key2)
    if additional_data is not None:
        st.subheader("A Display Of The Data Used to Train the Models Merged")
        st.dataframe(additional_data.head(50))

        # Provide download options for merged data
        st.subheader("Download File")
        xlsx_buf = io.BytesIO()
        with pd.ExcelWriter(xlsx_buf, engine='xlsxwriter') as writer:
            additional_data.to_excel(writer, index=False)
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
        fig_merged = create_plot(additional_data)
        buf_merged = plot_to_image(fig_merged)
        st.download_button(
            label="Download Image",
            data=buf_merged,
            file_name='merged_data_plot.png',
            mime='image/png'
        )

    # Additional sections for other CSV data (as per your original code)
    # Load and display test data
    test_data = load_csv_from_s3(csv_file_key3)
    if test_data is not None:
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
    predict_data = load_csv_from_s3(csv_file_key4)
    if predict_data is not None:
        st.subheader("A Display Of The Data Used in Testing the Machine Learning Models with the predicted values")
        st.dataframe(predict_data.head(50))

        # Provide download options for test data with predicted column
        st.subheader("Download CSV File with churn column")
        csv_pred = predict_data.to_csv(index=False)
        st.download_button(
            label="Download",
            data=csv_pred,
            file_name='test_data_with_predictions.csv',
            mime='text/csv'
        )

# Add copyright notice
    st.write("---")
    st.write("© 2024 Japan Machine Training Ltd. All Rights Reserved.")


# Call the data_page function when the module is run
if __name__ == "__main__":
    data_page()

import streamlit as st
import yaml
import pandas as pd
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import os

# Function to load history from S3
def load_history_from_s3():
    bucket_name = os.getenv("AWS_BUCKET_NAME")
    s3_file_name = "prediction_history.yaml"  # File in the S3 bucket

    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION"),
    )

    try:
        # Fetch the file from S3
        response = s3.get_object(Bucket=bucket_name, Key=s3_file_name)
        file_content = response['Body'].read().decode('utf-8')
        history = yaml.safe_load(file_content)
        return history

    except s3.exceptions.NoSuchKey:
        st.error("Prediction history file not found in S3.")
        return None
    except (NoCredentialsError, ClientError) as e:
        st.error(f"Error downloading prediction history from S3: {str(e)}")
        return None


def history_page():
    # Set the logo and title
    col1, col2 = st.columns([1, 10])  # Adjust the width ratio to balance logo and title
    with col1:
        st.image("logo/Logo.png", width=100)
        
    with col2:
        st.markdown("<h1 style='font-size: 58px;'>Japan Machine Training Ltd</h1>", unsafe_allow_html=True)

    st.write(" ### Prediction History")
    
    # Load the history from S3
    history = load_history_from_s3()
    if history is None or len(history) == 0:
        st.write("No prediction history found.")
        return

    # Display the prediction history
    for i, record in enumerate(history):
        st.write(f"### Prediction {i+1}")
        st.write(f"**Model Used:** {record['model']}")
        st.write("**Predictions:**")
        st.write(pd.DataFrame(record['data']))

    st.write("---")
    st.write("© 2024 Japan Machine Training Ltd. All Rights Reserved.")

# Render the history page
history_page()

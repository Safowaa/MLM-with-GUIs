import streamlit as st
import yaml
import pandas as pd
import boto3
from io import BytesIO
from botocore.exceptions import NoCredentialsError, ClientError
import os

# S3 setup
def get_s3_client():
    return boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION"),
    )

def load_history_from_s3():
    bucket_name = os.getenv("AWS_BUCKET_NAME")
    s3_file_name = "prediction_history.yaml"

    s3 = get_s3_client()

    try:
        response = s3.get_object(Bucket=bucket_name, Key=s3_file_name)
        file_content = response['Body'].read().decode('utf-8')
        history = yaml.safe_load(file_content) or []
        return history
    except s3.exceptions.NoSuchKey:
        st.error("Prediction history file not found in S3.")
        return []
    except (NoCredentialsError, ClientError) as e:
        st.error(f"Error downloading prediction history from S3: {str(e)}")
        return []

# Function to save updated history (only 15 records)
def save_history_to_s3(history):
    bucket_name = os.getenv("AWS_BUCKET_NAME")
    s3_file_name = "prediction_history.yaml"

    s3 = get_s3_client()

    # Limit history to the latest 15 entries
    history = history[:15]

    try:
        # Convert to YAML format
        history_yaml = yaml.safe_dump(history)

        # Upload to S3
        s3.put_object(Bucket=bucket_name, Key=s3_file_name, Body=history_yaml)
    except (NoCredentialsError, ClientError) as e:
        st.error(f"Error uploading prediction history to S3: {str(e)}")

# History Page
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

    if not history:
        st.write("No prediction history found.")
        return

    # Show only the first 15 predictions
    limited_history = history[:15]

    # Display the first 15 predictions
    for i, record in enumerate(limited_history, start=1):
        st.write(f"### Prediction {i}")
        st.write(f"**Model Used:** {record['model']}")
        st.write("**Predictions:**")
        st.write(pd.DataFrame(record['data']))

    # Provide a button to download all predictions as CSV
    if st.button("Download All Predictions"):
        all_history_df = pd.concat([pd.DataFrame(record['data']) for record in history], ignore_index=True)
        csv_data = all_history_df.to_csv(index=False)

        st.download_button(
            label="Download Predictions",
            data=csv_data,
            file_name='prediction_history.csv',
            mime='text/csv'
        )

    # Saving only the latest 15 records to the YAML file
    save_history_to_s3(history)

    st.write("---")
    st.write("© 2024 Japan Machine Training Ltd. All Rights Reserved.")

# Render the history page
history_page()

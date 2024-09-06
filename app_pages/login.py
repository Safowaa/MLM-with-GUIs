import streamlit as st
import yaml
import os
import boto3

# Function to download users.yaml from S3 bucket
def download_users_yaml_from_s3():
    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_REGION')
    )
    s3_bucket_name = 'mlmyamlbucket'  # Replace with your bucket name
    s3_file_key = 'users.yaml'  # The S3 key for the file (path in the bucket)

    try:
        s3_client.download_file(s3_bucket_name, s3_file_key, 'users.yaml')
        # st.write("Successfully downloaded users.yaml from S3.")
    except Exception as e:
        st.error(f"Error downloading users.yaml from S3: {e}")

# Function to upload users.yaml to S3 bucket
def upload_users_yaml_to_s3():
    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_REGION')
    )
    s3_bucket_name = 'mlmyamlbucket'  # Replace with your bucket name
    s3_file_key = 'users.yaml'  # The S3 key for the file (path in the bucket)

    try:
        s3_client.upload_file('users.yaml', s3_bucket_name, s3_file_key)
        st.write("Successfully uploaded users.yaml to S3.")
    except Exception as e:
        st.error(f"Error uploading users.yaml to S3: {e}")

def login():
    # Download the users.yaml file from S3
    download_users_yaml_from_s3()

    # Set the logo and title
    col1, col2 = st.columns([1, 10])  # Adjust the width ratio to balance logo and title
    with col1:
        st.image("logo/Logo.png", width=100)

    with col2:
        st.markdown("<h1 style='font-size: 58px;'>Japan Machine Training Ltd</h1>", unsafe_allow_html=True)

    st.subheader("Please login to access the application.")

    # Create two columns for the login and create account sections
    col1, col2 = st.columns([1, 1])
    
    # Login section
    with col1:
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')

        if st.button("Login"):
            if username and password:
                # Load existing users from the downloaded YAML file
                if os.path.exists('users.yaml'):
                    with open('users.yaml', 'r') as file:
                        users = yaml.safe_load(file) or {}
                else:
                    users = {}

                if username in users and users[username] == password:
                    st.session_state['logged_in'] = True
                    st.session_state['username'] = username
                    st.success("Logged in successfully!")
                    st.experimental_rerun()  # Rerun to show the main page
                else:
                    st.warning("Incorrect username or password. Please try again.")
            else:
                st.warning("Please enter a username and password.")

    # Create account section
    with col2:
        st.subheader("Create a new account")
        new_username = st.text_input("New Username", key="new_username")
        new_password = st.text_input("New Password", type='password', key="new_password")

        if st.button("Register"):
            if new_username and new_password:
                # Load existing users from the downloaded YAML file
                if os.path.exists('users.yaml'):
                    with open('users.yaml', 'r') as file:
                        users = yaml.safe_load(file) or {}
                else:
                    users = {}

                if new_username in users:
                    st.warning("Username already exists. Please choose another.")
                else:
                    users[new_username] = new_password
                    with open('users.yaml', 'w') as file:
                        yaml.dump(users, file)
                    st.success("Account created! Please log in.")

                    # Upload the updated users.yaml back to S3
                    upload_users_yaml_to_s3()
            else:
                st.warning("Please fill out all fields.")

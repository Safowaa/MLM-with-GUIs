import streamlit as st
import yaml
import os


def login():
    # Set the logo and title
    col1, col2 = st.columns([1, 10])  # Adjust the width ratio to balance logo and title
    with col1:
        st.image("logo/Logo.png", width=100)
        
    with col2:
        st.markdown("<h1 style='font-size: 58px;'>Japan Machine Training Ltd</h1>", unsafe_allow_html=True)

    st.subheader("Please login to access the application.")
    
    
    # Create two columns for the login and create account sections
    col1, col2 = st.columns([1,1])
    with col1:
        # Login section
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')

        if st.button("Login"):
            if username and password:
                # Load existing users from YAML file
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

    with col2:
        # Create account section
        st.subheader("Create a new account")
        new_username = st.text_input("New Username", key="new_username")
        new_password = st.text_input("New Password", type='password', key="new_password")

        if st.button("Register"):
            if new_username and new_password:
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
            else:
                st.warning("Please fill out all fields.")


import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Japan Machine Training Ltd (TCCPA)", 
    page_icon="logo/Logo.png",
    layout="wide"
)
# Sidebar for navigation
st.sidebar.title("Menu")

# Define the available pages
pages = {
    "📑Login": "login.py",
    "🛖Home": "app_pages/main_page.py",
    "📊Dashboard": "app_pages/dashboard.py",
    "📈🏠DataHouse": "app_pages/data_page.py",
    "👨🏾‍🔧Predict": "app_pages/predict_page.py",
    "🔁History": "app_pages/history_page.py",
}

# Create a sidebar for navigation
selection = st.sidebar.selectbox("Go to", list(pages.keys()))

# Ensure the user is logged in or display the login page
if selection == "📑Login":
    from app_pages.login import login
    login()
elif 'logged_in' in st.session_state and st.session_state['logged_in']:
    # Import and run the selected page
    if selection == "🛖Home":
        from app_pages.main_page import main_page
        main_page()
    elif selection == "📊Dashboard":
        from app_pages.dashboard import dashboard_page
        dashboard_page()
    elif selection == "📈🏠DataHouse":
        from app_pages.data_page import data_page
        data_page()
    elif selection == "👨🏾‍🔧Predict":
        from app_pages.predict_page import predict_page
        predict_page()
    elif selection == "🔁History":
        from app_pages.history_page import history_page
        history_page()
else:
    st.warning("Please log in to access the application.")

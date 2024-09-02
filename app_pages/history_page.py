import streamlit as st
import yaml
import pandas as pd

def history_page():
    # Set the logo and title
    col1, col2 = st.columns([1, 10])  # Adjust the width ratio to balance logo and title
    with col1:
        st.image("logo/Logo.png", width=100)
        
    with col2:
        st.markdown("<h1 style='font-size: 58px;'>Japan Machine Training Ltd</h1>", unsafe_allow_html=True)

    st.write(" ### Prediction History")
    
    try:
        with open("prediction_history.yaml", "r") as file:
            history = yaml.safe_load(file)
            if not history:
                st.write("No prediction history found.")
                return

            for i, record in enumerate(history):
                st.write(f"### Prediction {i+1}")
                st.write(f"**Model Used:** {record['model']}")
                st.write("**Predictions:**")
                st.write(pd.DataFrame(record['data']))

    except FileNotFoundError:
        st.write("No prediction history file found.")

    st.write("---")
    st.write("© 2024 Japan Machine Training Ltd. All Rights Reserved.")

# Render the history page
history_page()

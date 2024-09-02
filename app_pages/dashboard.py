import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns

def dashboard_page():
    # Set the logo and title
    col1, col2 = st.columns([1, 10])  # Adjust the width ratio to balance logo and title
    with col1:
        st.image("logo/Logo.png", width=100)
        
    with col2:
        st.markdown("<h1 style='font-size: 58px;'>Japan Machine Training Ltd</h1>", unsafe_allow_html=True)

    st.write(" ## Telco Customer Attrition Dashboard")
    st.write(" ##### Visualizations From Python Notebooks and The Projects PowerBI Dashboard")
    st.write("Analysis was performed to understand the distribution of data, detect anomalies, and identify relationships between features.")
    
    # Load data
    data = pd.read_csv(r'data_files\train_data.csv')

    # Line chart: Tenure over MonthlyCharges
    st.write(" ### Line Chart of Tenure over Monthly Charges")
    st.line_chart(data[['tenure', 'MonthlyCharges']])

    # Bar chart: Churn by Contract
    st.write(" ### Bar Chart of Churn by Contract Type")
    churn_contract = data.groupby('Contract')['Churn'].value_counts(normalize=True).unstack().fillna(0)
    st.bar_chart(churn_contract)

    # Pie chart: Gender Distribution
    st.write(" ### Pie Chart of Gender Distribution")
    gender_counts = data['gender'].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)

    # Scatter plot: Total Charges vs. Monthly Charges
    st.write(" ### Scatter Plot of Total Charges vs. Monthly Charges")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(x='MonthlyCharges', y='TotalCharges', hue='Churn', data=data, ax=ax2)
    st.pyplot(fig2)

    # Histogram: Distribution of Tenure
    st.write(" ### Histogram of Distribution of Tenure")
    fig3, ax3 = plt.subplots()
    sns.histplot(data['tenure'], bins=20, kde=True, ax=ax3)
    st.pyplot(fig3)

    # Boxplot: Monthly Charges by Contract Type
    st.write(" ### Boxplot of Monthly Charges by Contract Type")
    fig4, ax4 = plt.subplots()
    sns.boxplot(x='Contract', y='MonthlyCharges', data=data, ax=ax4)
    st.pyplot(fig4)

    st.write(" ## Below are the visuals from the Python NoteBook ")

    # List of image paths (after the charts)
    image_paths = [
        r"dashboard_images\Dashboard.png",
        r"dashboard_images\churn_by_contract_type.png",
        r"dashboard_images\churn_by_tech_support.png",
        r"dashboard_images\churn_by_seniorCitizen.png",
        r"dashboard_images\churn_by_gender.png",
        r"dashboard_images\correlation_numeric.png",
        r"dashboard_images\churn.png",
        r"dashboard_images\Tenure_by_churn.png",
        r"dashboard_images\churn_by_internet.png"
    ]

    # Placeholder for the image
    image_placeholder = st.empty()
    
    

    # Endless slideshow loop
    while True:
        for image_path in image_paths:
            image_placeholder.image(image_path, use_column_width=True)
            time.sleep(10)  # Display each image for 10 seconds
            
            
        st.write("Interact and view more insights on PowerBI using the link below")
        st.markdown("""
        <a href="https://app.powerbi.com/groups/me/reports/a814a603-ddbe-4f36-8c6e-674ecd59f05b/ReportSection?experience=power-bi" target="_blank">
        <button style="background-color:#D8C04E; color:black; border:none; padding:10px 90px; text-align:center; font-size:16px; margin:2px; cursor:pointer; border-radius:5px;">
        PowerBI
        </button>
        """, unsafe_allow_html=True)

        st.write("---")
        # Add copyright notice
        st.write("© 2024 Japan Machine Training Ltd. All Rights Reserved.")

# Run the dashboard
if __name__ == "__main__":
    dashboard_page()

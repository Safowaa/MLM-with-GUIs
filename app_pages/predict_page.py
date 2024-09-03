import streamlit as st
import pandas as pd
import joblib
import yaml

def save_prediction_to_history(input_data, y_pred, model_choice):
    # Load the existing history
    try:
        with open("prediction_history.yaml", "r") as file:
            history = yaml.safe_load(file)
            if history is None:
                history = []
    except FileNotFoundError:
        history = []

    # Prepare the prediction record
    input_data['Predicted_Churn'] = ['Yes' if x == 1 else 'No' for x in y_pred]
    prediction_record = {
        "model": model_choice,
        "data": input_data.to_dict(orient='records')
    }

    # Append the new prediction to history
    history.append(prediction_record)

    # Save the updated history
    with open("prediction_history.yaml", "w") as file:
        yaml.safe_dump(history, file)

def predict_page():
    
    # Set the logo and title
    col1, col2 = st.columns([1, 10])  # Adjust the width ratio to balance logo and title
    with col1:
        st.image("logo/Logo.png", width=100)
        
    with col2:
        st.markdown("<h1 style='font-size: 58px;'>Japan Machine Training Ltd</h1>", unsafe_allow_html=True)
        
    st.write(" ## Determin if your customer will or will not churn.")
    
    st.write(" ##### Please Note: The CSV / Excel file you upload should have strictly the below.")
    st.write("""
    <p style="color:red;">
        The following columns should have these features Yes/No only, Senior Citizen, Partner, Dependents, Phone Service, Multiple Lines, Online Security, Online Backup, Device Protection, Tech Support, Streaming TV, Streaming Movies, and Paperless Billing. The numeric columns are: Tenure (Months), Monthly Charges, and Total Charges. Other columns, Gender should have Male and Female, Internet Service should have DSL, Fiber Optic, and No, Contract should have Month-to-Month, One year, and Two year, Payment Method should have Electronic check, Mailed check, and Bank transfer.
    </p>
           """, unsafe_allow_html=True)


    # Model selection
    st.write(" ### Choose a model to use for prediction:")
    model_choice = st.radio("First and Second Best Performing Models", ("Logistic Regression", "Random Forest")
    )

    # File upload option
    file_choice = st.radio(
        "Choose a file input method:",
        ("Upload a CSV or Excel file","Use existing Excel file")
    )

    # Load the preprocessor pipeline
    preprocessor_pipeline = joblib.load(r'pipeline\preprocessor_pipeline.pkl')

    # Load the models
    logistic_regression_model = joblib.load(r'models\logistic_regression_model.pkl')
    random_forest_model = joblib.load(r'models\random_forest_model.pkl')

    # Choose file based on the user's selection
    if file_choice == "Use existing Excel file":
        file_path = r"data_files\Telco-churn-last-2000.xlsx"
        input_data = pd.read_excel(file_path)
    else:
        uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])
        if uploaded_file is not None:
            if uploaded_file.name.endswith('.csv'):
                input_data = pd.read_csv(uploaded_file)
            else:
                input_data = pd.read_excel(uploaded_file)
        else:
            st.error("Please upload a file to continue.")
            st.stop()

    if input_data is not None:
        # Preprocess and make predictions
        X_input = preprocessor_pipeline.transform(input_data)
        st.write("Preprocessing successful!")

        # Predict using the chosen model
        if model_choice == "Logistic Regression":
            y_pred = logistic_regression_model.predict(X_input)
        else:
            y_pred = random_forest_model.predict(X_input)

        # Save the prediction to history
        save_prediction_to_history(input_data, y_pred, model_choice)

        # Add the predictions to the input data
        input_data['Predicted_Churn'] = ['Yes' if x == 1 else 'No' for x in y_pred]

        # Display the predictions
        st.write("### Predictions:")
        st.write(input_data)

    st.write("---")
    st.write("© 2024 Japan Machine Training Ltd. All Rights Reserved.")

# Render the prediction page
predict_page()

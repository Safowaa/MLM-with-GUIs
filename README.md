## Telco Customer Churn Prediction Web App


## Overview
 This project is a web application developed using Streamlit and Python, designed to predict customer churn for telecommunications companies. By leveraging machine learning models, the app provides insights into customer behavior, enabling businesses to take proactive measures to retain their customers.
- Access the deployed app on [Render](https://mlm-with-guis.onrender.com/)
- Read more on this project on [Meduim](https://medium.com/@safowaabenedicta/embedding-machine-learning-models-in-web-apps-2913d2c31533)

## **Features**
![.](https://github.com/Safowaa/MLM-with-GUIs/blob/master/readmePictures/Screenshot%202024-09-21%20163448.png)
![.](https://github.com/Safowaa/MLM-with-GUIs/blob/master/readmePictures/Screenshot%202024-09-01%20202247.png)
![.](https://github.com/Safowaa/MLM-with-GUIs/blob/master/readmePictures/Screenshot%202024-09-01%20202147.png)
![.](https://github.com/Safowaa/MLM-with-GUIs/blob/master/readmePictures/Screenshot%202024-09-01%20202128.png)
![.](https://github.com/Safowaa/MLM-with-GUIs/blob/master/readmePictures/Screenshot%202024-09-01%20202059.png)


- User-Friendly Interface: Intuitive design that allows users to easily navigate through the app.

- Predict Page: Upload customer data and receive churn predictions instantly.

- Dashboard: Visualize key metrics and trends related to customer churn.

- Data Page: Access and explore datasets used in the analysis.

- Secure Login: Protect sensitive information with user authentication.


## **Technologies Used**

- Python: The core programming language for building the application.
- Streamlit: Framework used to create the web interface.
- Pandas: For data manipulation and analysis.
- Scikit-learn: For building and evaluating machine learning models.
- Docker: For containerizing the application for easy deployment.
- Project Structure


``` bash
├── .streamlit
│   └── config.toml
├── app_pages
│   ├── __pycache__
│   ├── dashboard.py
│   ├── data_page.py
│   ├── history_page.py
│   ├── login.py
│   ├── main_page.py
│   └── predict_page.py
├── dashboard_images
│   ├── Dashboard.png
│   ├── EDA-correlation.png
│   ├── Tenure_by_churn.png
│   ├── churn.png
│   ├── churn_by_contract_type.png
│   ├── churn_by_gender.png
│   ├── churn_by_internet.png
│   ├── churn_by_paymentmethod.png
│   ├── churn_by_seniorCitizen.png
│   ├── churn_by_tech_support.png
│   └── correlation_numeric.png
├── data_files
│   ├── LP2_Telco-churn-second-2000.csv
│   ├── Telco-churn-last-2000.xlsx
│   ├── test_data_with_predictions.csv
│   └── train_data.csv
├── logo
│   └── Logo.png
├── models
│   ├── logistic_regression_model.pkl
│   └── random_forest_model.pkl
├── pipeline
│   └── preprocessor_pipeline.pkl
├── team_pictures
│   ├── Josephine1.png
│   ├── Safowaa1.png
│   ├── Teampic1.jpg
│   └── teampic2.jpg
├── .gitignore
├── Dockerfile
├── LICENSE
├── README.md
├── app.py
├── docker-compose.yaml
└── requirements.txt
```

### Installation
Clone the repository:
```bash
git clone https://github.com/Safowaa/MLM-with-GUIs.git
```

#### Navigate to the project directory:
```bash
cd MLM-with-GUIs.git
```

#### Install the required packages:
```bash
pip install -r requirements.txt
```

### Run the app:
```bash

streamlit run app.py
```

### Deployment

The application is containerized using Docker. To build and run the Docker container, use the following commands:

### Contributing

Contributions are welcome! Please open an issue or submit a pull request if you would like to contribute.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments

Special thanks to [Azubi Africa](https://www.azubiafrica.org/data-analytics?utm_source=medium,linkedin&utm_medium=articles&utm_campaign=DAP+Learners) for their support and training.

Inspiration and resources from the DAP7 of [Azubi Arica](https://www.azubiafrica.org/data-analytics?utm_source=medium,linkedin&utm_medium=articles&utm_campaign=DAP+Learners).

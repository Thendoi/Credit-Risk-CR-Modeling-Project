# Credit Risk Scorecard Project

A credit risk scorecard is a predictive model used by financial institutions to evaluate the creditworthiness of loan applicants. It supports consistent and data-driven lending decisions by estimating the likelihood that a customer will repay their debt. Credit scorecards are widely applied in credit approval, portfolio monitoring, risk management, and the estimation of expected credit losses.

This project uses a historical credit dataset containing customer demographic, financial, and loan-related information, together with each customer's repayment outcome. The dataset includes variables such as age, income, savings and checking account status, loan amount, loan duration, employment status, and other characteristics that may influence credit risk.

Machine learning classification models, including **Logistic Regression**, **Random Forest**, and **XGBoost**, are developed and evaluated to classify customers as either **good** or **bad** credit risks. Model performance is assessed using metrics such as Accuracy, AUC, Gini Coefficient, and the KS Statistic. The best-performing model can then be used to score new loan applicants, enabling lenders to make informed credit decisions while managing portfolio risk and reducing the likelihood of defaults.

 # Business Problem

Financial institutions face significant losses due to loan defaults and poor credit decisions.

This project helps:

-  Identify high-risk customers 

-  Improve loan approval decisions 

-  Reduce financial risk Support explainable AI decision-making  SHAP Explainability

The project integrates SHAP (SHapley Additive exPlanations) to provide transparent model predictions.


# Project Overview  

This project is an end-to-end Machine Learning based Credit Risk Prediction System developed using Python, XGBoost, SHAP Explainability, and Streamlit.

The model classifies each applicant into one of the following categories:

- ✅ **Good Credit Customer**
- ❌ **Bad Credit Customer**


The project also includes model explainability using SHAP values, allowing users to understand which features contribute most to prediction outcomes.

# Live Features

- ✅ Credit Risk Prediction
- ✅ Interactive Streamlit Dashboard
- ✅ SHAP Explainability
- ✅ Feature Importance Visualization
- ✅ Risk Probability Gauge
- ✅ Download Prediction Results
- ✅ End-to-End ML Workflow
- ✅ Business Insights Section

# Machine Learning Workflow

The project follows a complete machine learning lifecycle:

# Data Collection

- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Feature Engineering
- Model Training
- Model Evaluation
- Explainable AI (SHAP)
- Streamlit Deployment

# Models Used
The following models were trained and evaluated:

| Model | Accuracy | ROC-AUC |
|--------|---------:|--------:|
| Logistic Regression | **42%** | **0.50** |
| Random Forest | 42% | 0.43 |
| XGBoost | 39% | 0.44 |

**Logistic Regression** was selected as the final production model based on superior performance.

# Evaluation Metrics
The project includes:

- Accuracy
- ROC Curve
- AUC Score
- Confusion Matrix
- KS Statistic
- Feature Importance
- SHAP Explainability


# Prediction App (Web Application) 

<img width="2539" height="1041" alt="C1" src="https://github.com/user-attachments/assets/6c5bc05f-d1b0-49d6-bde9-bac1d5726f48" />

<img width="2544" height="1374" alt="C2" src="https://github.com/user-attachments/assets/e3e10d1e-d8ba-43c5-88bc-cecdee2f6698" />

<img width="2551" height="1072" alt="C3" src="https://github.com/user-attachments/assets/b9879778-d602-4499-840c-b3bc3f2be358" />

<img width="1268" height="596" alt="C4" src="https://github.com/user-attachments/assets/3c7fe757-9e24-4753-9aad-9d5460933ed7" />

<img width="2542" height="1267" alt="C6" src="https://github.com/user-attachments/assets/e1885187-4320-49b7-ab3c-0da36f600f0a" />

<img width="914" height="167" alt="C7" src="https://github.com/user-attachments/assets/eb55a784-2162-4c68-91a5-3d243f1fcdca" />



# Project Structure

Credit-Risk(CR)-Modeling-Project/ │ ├── app/ │ └── streamlit_app.py │ ├── data/ │ ├── raw/ │ └── processed/ │ ├── models/ │ ├── logistic_regression.pkl │ ├── random_forest.pkl │ ├── xgboost_model.pkl │ └── scaler.pkl │ ├── notebooks/ │ ├── 01_EDA.ipynb │ ├── 02_Preprocessing.ipynb │ ├── 03_Modeling.ipynb │ └── 04_Evaluation.ipynb │ ├── requirements.txt └── README.md











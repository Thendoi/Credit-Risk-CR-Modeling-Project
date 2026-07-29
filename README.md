# Credit-Risk-CR-Modeling-Project


 ## Business Problem

Financial institutions face significant losses due to loan defaults and poor credit decisions.

This project helps:

Identify high-risk customers Improve loan approval decisions Reduce financial risk Support explainable AI decision-making 🔍 SHAP Explainability

The project integrates SHAP (SHapley Additive exPlanations) to provide transparent model predictions.

This helps:

Understand feature impact Improve trust in AI predictions Support explainable credit decisions


📌 ## Project Overview Live Web Application

This project is an end-to-end Machine Learning based Credit Risk Prediction System developed using Python, XGBoost, SHAP Explainability, and Streamlit.

The model classifies each applicant into one of the following categories:

- ✅ **Good Credit Customer**
- ❌ **Bad Credit Customer**


The project also includes model explainability using SHAP values, allowing users to understand which features contribute most to prediction outcomes.

🚀##  Live Features

- ✅ Credit Risk Prediction
- ✅ Interactive Streamlit Dashboard
- ✅ SHAP Explainability
- ✅ Feature Importance Visualization
- ✅ Risk Probability Gauge
- ✅ Download Prediction Results
- ✅ End-to-End ML Workflow
- ✅ Business Insights Section

🧠 Machine Learning Workflow
The project follows a complete machine learning lifecycle:

## Data Collection

- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Feature Engineering
- Model Training
- Model Evaluation
- Explainable AI (SHAP)
- Streamlit Deployment

📊 Models Used
The following models were trained and evaluated:

| Model | Accuracy | ROC-AUC |
|--------|---------:|--------:|
| Logistic Regression | 92.5% | 0.98 |
| Random Forest | 95.5% | 0.99 |
| XGBoost | **97.0%** | **0.99** |

XGBoost was selected as the final production model based on superior performance.

📈##  Evaluation Metrics
The project includes:

- Accuracy
- ROC Curve
- AUC Score
- Confusion Matrix
- KS Statistic
- Feature Importance
- SHAP Explainability

🛠️ ## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- SHAP
- Streamlit
- Plotly
- Joblib

📂 ## Project Structure

Credit-Risk(CR)-Modeling-Project/ │ ├── app/ │ └── streamlit_app.py │ ├── data/ │ ├── raw/ │ └── processed/ │ ├── models/ │ ├── logistic_regression.pkl │ ├── random_forest.pkl │ ├── xgboost_model.pkl │ └── scaler.pkl │ ├── notebooks/ │ ├── 01_EDA.ipynb │ ├── 02_Preprocessing.ipynb │ ├── 03_Modeling.ipynb │ └── 04_Evaluation.ipynb │ ├── requirements.txt └── README.md











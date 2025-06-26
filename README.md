# 🧠 Health Insurance Premium Prediction
A predictive machine learning model to estimate health insurance premiums based on user attributes such as age, BMI, smoking status, and medical history.  
Developed as part of an MLOps-focused portfolio project, it includes training notebooks, model artifacts, a Streamlit web interface, and is cloud-deployment ready.

---

## 🚀 Key Features

- ✔️ Supervised ML models trained on real insurance data
- 🧪 Data segmentation: youth vs adults, with/without genetic risk
- 📦 Serialized models and scalers for reproducibility
- 🌐 Streamlit interface for real-time prediction
- 📁 Modular and clean repository layout

---

## 🗂️ Project Structure

```bash
insurance-premium-prediction/
├── app/                    # Streamlit web app
│   ├── main.py
│   └── prediction_helper.py
├── artifacts/              # Trained model + scaler (joblib)
│   ├── model_adults.joblib
│   ├── model_youth.joblib
│   ├── scaler_adults.joblib
│   └── scaler_youth.joblib
├── data/
│   └── raw/                # Raw Excel files used for training
├── notebooks/             # Notebooks for EDA, training, evaluation
│   ├── 01_global_model_training.ipynb
│   ├── 02_data_segmentation.ipynb
│   ├── 03_model_training_youth.ipynb
│   ├── 04_model_training_adults.ipynb
│   ├── 05_model_training_youth_with_genetical_risk.ipynb
│   └── 06_model_training_adults_with_genetical_risk.ipynb
├── requirements.txt        # Python dependencies
├── LICENSE
└── README.md               # This file


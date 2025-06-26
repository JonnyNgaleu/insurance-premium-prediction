# 🧠 Health Insurance Premium Prediction

A predictive machine learning model to estimate health insurance premiums based on user attributes such as age, BMI, smoking status, and medical history.  
Developed as part of an MLOps-focused portfolio project, it includes training notebooks, model artifacts, a Streamlit web interface, and is cloud-deployment ready.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://insurance-cost-predictor.streamlit.app/)
![CI](https://github.com/JonnyNgaleu/insurance-premium-prediction/actions/workflows/ci.yml/badge.svg)
---

## 🚀 Key Features

- ✔️ Supervised ML models trained on real insurance data
- 🧪 Data segmentation: youth vs adults, with/without genetic risk
- 📦 Serialized models and scalers for reproducibility
- 🌐 Streamlit interface for real-time prediction
- 📁 Modular and clean repository layout

---

## 🖼️ Live App Preview

![Streamlit App Screenshot](artifacts/live_app.png)

## 🗂️ Project Structure

```bash
insurance-premium-prediction/
├── .github/
│   └── workflows/
│       └── ci.yml                 # GitHub Actions CI workflow
├── app/                           # Streamlit web app
│   ├── main.py
│   └── prediction_helper.py
├── artifacts/                     # Trained models + visual assets
│   ├── model_adults.joblib
│   ├── model_youth.joblib
│   ├── scaler_adults.joblib
│   ├── scaler_youth.joblib
│   └── live_app.png               # Screenshot for live app
├── data/
│   └── raw/                       # Raw Excel files used for training
│       ├── premiums.xlsx
│       ├── premiums_adults.xlsx
│       ├── premiums_youth.xlsx
│       └── premiums_youth_with_gr.xlsx
├── notebooks/                    # Jupyter notebooks (EDA, training)
│   ├── 01_global_model_training.ipynb
│   ├── 02_data_segmentation.ipynb
│   ├── 03_model_training_youth.ipynb
│   ├── 04_model_training_adults.ipynb
│   ├── 05_model_training_youth_with_genetical_risk.ipynb
│   └── 06_model_training_adults_with_genetical_risk.ipynb
├── tests/                         # Unit tests (pytest)
│   └── test_prediction.py
├── .gitignore
├── requirements.txt               # Python dependencies
├── LICENSE
└── README.md


import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from app.prediction_helper import predict


def test_predict_valid_input():
    input_dict = {
        'Age': 30,
        'Number of Dependants': 2,
        'Income in Lakhs': 15,
        'Genetical Risk': 2,
        'Insurance Plan': 'Silver',
        'Employment Status': 'Salaried',
        'Gender': 'Male',
        'Marital Status': 'Married',
        'BMI Category': 'Normal',
        'Smoking Status': 'No Smoking',
        'Region': 'Northwest',
        'Medical History': 'No Disease'
    }

    prediction = predict(input_dict)

    assert isinstance(prediction, int), "Prediction should be an integer"
    assert prediction > 0, "Prediction should be a positive cost"
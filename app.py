# app.py

from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained pipeline
model = joblib.load('salary_prediction_pipeline.pkl')

# Expected columns (based on your training data)
expected_columns = [
    'AGE', 'LEAVES USED', 'LEAVES REMAINING', 'RATINGS', 'PAST EXP', 'COMPANY EXP',
    'SEX_M', 'DESIGNATION_Associate', 'DESIGNATION_Director', 'DESIGNATION_Manager', 
    'DESIGNATION_Senior Analyst', 'DESIGNATION_Senior Manager', 'UNIT_IT', 
    'UNIT_Management', 'UNIT_Marketing', 'UNIT_Operations', 'UNIT_Web'
]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        df = pd.DataFrame(data, index=[0])
        
        # Add missing columns with default value 0
        for col in expected_columns:
            if col not in df.columns:
                df[col] = 0
        
        # Reorder columns to match the training set
        df = df[expected_columns]
        
        prediction = model.predict(df)
        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

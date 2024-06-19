# test_api.py

import requests
import json

url = 'http://127.0.0.1:5000/predict'
data = {
    "AGE": 30,
    "LEAVES USED": 5,
    "LEAVES REMAINING": 15,
    "RATINGS": 4.5,
    "PAST EXP": 6,
    "COMPANY EXP": 2,
    "SEX_M": 1,
    "DESIGNATION_Associate": 0,
    "DESIGNATION_Director": 0,
    "DESIGNATION_Manager": 0,
    "DESIGNATION_Senior Analyst": 0,
    "DESIGNATION_Senior Manager": 0,
    "UNIT_IT": 0,
    "UNIT_Management": 0,
    "UNIT_Marketing": 0,
    "UNIT_Operations": 0,
    "UNIT_Web": 0
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.content)
print(response.json())

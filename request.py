import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json= {'age':18,	'sex':'M',	'cp':0,	'trestbps':150,	'chol':200,'fbs':1,'restecg':1,'thalach':159,'exang':0,'oldpeak':3.5,'slope':2,'ca':0,'thal':3})

print(r.json())

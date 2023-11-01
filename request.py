import requests
import json

url = "http://127.0.0.1:5000/predict"
data = {[]}  # Substitua "..." pelos dados de entrada

headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(data), headers=headers)

if response.status_code == 200:
    predictions = response.json()
    print("Previsões:", predictions)
else:
    print("Erro ao fazer previsão", response.json())
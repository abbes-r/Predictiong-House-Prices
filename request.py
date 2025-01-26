import requests

url = 'http://localhost:5000/predict_api'

input_data = {"area": 7150,
              "bedrooms": 3,
              "bathrooms": 2,
              "stories": 2,
              "mainroad": 0,
              "guestroom": 1,
              "basement": 0,
              "airconditioning": 1,
              "parking": 1,
              "prefarea": 0
}

r = requests.post(url,json=input_data)

print(r.json())
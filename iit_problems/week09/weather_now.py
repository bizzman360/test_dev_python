import requests

response = requests.get("[api.open-meteo.com/v1/forecast?latitude=6.9271​&amp;&​longitude=79.8612¤t_weather=true](https://api.open-meteo.com/v1/forecast?latitude=6.9271&longitude=79.8612&current_weather=true)").json()


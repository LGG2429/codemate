import requests

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=14.44&longitude=79.99&current_weather=true")

data = response.json()
print(data)

print("--"*10)

print("Current temperature:",data["current_weather"]["temperature"],"°C")

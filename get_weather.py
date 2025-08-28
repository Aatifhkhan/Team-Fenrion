import requests

API_KEY = "170ad135794af4df80fe182a7ded7fcd"  # your key
CITY = "Bengaluru"  # you can change this to your city

URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    rainfall = data.get("rain", {}).get("1h", 0)  # rain in last 1 hour

    print("City:", CITY)
    print("Temperature:", temp, "°C")
    print("Rainfall:", rainfall, "mm")
    print("Humidity:", humidity, "%")
else:
    print("Error:", data)

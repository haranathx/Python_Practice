import requests
import csv

# API URL (London weather)
url = "https://api.open-meteo.com/v1/forecast?latitude=51.5072&longitude=-0.1276&current=temperature_2m,relative_humidity_2m,wind_speed_10m"

print("Connecting to API...")

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

current = data["current"]

temperature = current["temperature_2m"]
humidity = current["relative_humidity_2m"]
wind = current["wind_speed_10m"]

print("Temperature:", temperature)
print("Humidity:", humidity)
print("Wind:", wind)

with open("weather.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Temperature",
        "Humidity",
        "Wind Speed"
    ])

    writer.writerow([
        temperature,
        humidity,
        wind
    ])

print("CSV Saved Successfully!")
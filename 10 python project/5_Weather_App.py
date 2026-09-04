import requests

longitude = input("Enter the Longitude: ")
latitude = input("Enter the latitude: ")

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&models=jma_seamless"

print(url)

r = requests.get(url)

data = r.json()

hourly = data['hourly']
times = hourly["time"]
temperatures = hourly["temperature_2m"]

print(f"{'Time':<20} {'Temperature(°C)'}")
print('-'*40)
for time, temp in zip(times, temperatures):
    print(f"{time:<20}  {temp}°C")
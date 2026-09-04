import requests

city_name = input("Enter the City Name: ")

# Geocoding API to get coordinates from city name
geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"

geo_response = requests.get(geo_url) # Send request to the geocoding API
geo_data = geo_response.json()       # Convert the response into Python dictionary
print(geo_url)

try:
     # Check if the API returned any results
    if geo_data['results']:
        # Get latitude, longitude, and city name from the first result
        latitude = geo_data['results'][0]['latitude']
        longitude = geo_data['results'][0]['longitude']
        city = geo_data['results'][0]['name']

        print(f"\nGetting information for {city}\n")
         
        # Build the weather API URL using the city coordinates
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&models=jma_seamless"
            
        r = requests.get(weather_url)       # Send request to the weather API
        data = r.json()        # Convert weather response to JSON
        print(weather_url)     # Print the weather URL for debugging

        # Get hourly weather data
        hourly = data['hourly']

        # Extract time and temperature lists
        times = hourly['time']
        temperatures = hourly['temperature_2m']

        print(f"{'Time':<20} {'Temperature(°C)'}")
        print('\n','-'*40,'\n')

        for time, temp in zip(times, temperatures):
            print(f"{time:<20} {temp}°C")

    else:
        print("City doesn't exists!")

except Exception as e:
    print(f"Error: {e}")
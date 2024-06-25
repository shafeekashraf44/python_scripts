import requests

# API endpoint
url = "https://api.ambeedata.com/latest/by-lat-lng"

# Parameters
params = {
    'lat': 12,
    'lng': 77
}

# Headers
headers = {
    'x-api-key': '1f2eFcCA8a53dc9AA08B68f5B5eE6B4abD2A3Bd55823Fb79',
    'Content-type': 'application/json'
}

# Making the GET request
response = requests.get(url, headers=headers, params=params)

# Checking if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Parsing the JSON response
    if data['message'] == 'success' and 'stations' in data:
        for station in data['stations']:
            AQI = station.get('AQI', 'N/A')
            category = station.get('aqiInfo', {}).get('category', 'N/A')
            timestamp = station.get('updatedAt', 'N/A')
            dominant_pollutant = station.get('aqiInfo', {}).get('pollutant', 'N/A')
            
            print(f"The air quality level will be {category} with AQI:{AQI} at {timestamp} with the dominant pollutant being {dominant_pollutant}")
    else:
        print("No stations data found in the response.")
else:
    print(f"Error: {response.status_code}, {response.text}")

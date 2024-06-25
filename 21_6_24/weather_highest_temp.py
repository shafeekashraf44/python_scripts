import requests

# API endpoint
url = "https://api.ambeedata.com/weather/history/by-lat-lng"

# Parameters
params = {
    'lat': 12,
    'lng': 77,
    'from': '2024-06-24 00:00:00',
    'to': '2024-06-25 00:00:00'
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

    # Debug: Print the keys at the top level
    print("Top-level keys in the response:", data.keys())
    
    # Extracting the 'history' data from the response
    history_data = data.get('data', {}).get('history', [])

    if history_data:
        highest_temp = None
        highest_temp_timestamp = None
        
        # Iterating through each entry in the history data
        for entry in history_data:
            # Extract temperature and timestamp
            temp = entry.get('temperature')
            timestamp = entry.get('createdAt')

            # If temperature is found and it's higher than current highest_temp
            if temp is not None and (highest_temp is None or temp > highest_temp):
                highest_temp = temp
                highest_temp_timestamp = timestamp
        
        # Printing the result if highest temperature is found
        if highest_temp is not None:
            print(f"The highest temperature was {highest_temp}°C at {highest_temp_timestamp}.")
        else:
            print("No temperature data found in the response history.")
    else:
        print("No history data found in the response.")
else:
    print(f"Error: {response.status_code}, {response.text}")

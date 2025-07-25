# import requests
# from weather_api_key import key2  # ensure weather_api_key.py contains: key2 = "your_key"

# def get_weather(city="Kurnool"):
#     api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key2}&units=metric"
#     response = requests.get(api_url)
    
#     if response.status_code == 200:
#         json_data = response.json()
#         temperature = round(json_data["main"]["temp"], 1)
#         description = json_data["weather"][0]["description"]
#         return temperature, description
#     else:
#         print(f"Error {response.status_code}: {response.json().get('message', 'Unknown error')}")
#         return None, None

# # Example usage
# temp, desc = get_weather()
# if temp is not None:
#     print(f"The temperature is {temp}°C with {desc}")

import requests
from weather_api_key import key2
api_address ="https://api.openweathermap.org/data/2.5/weather?q=Kurnool&appid="+key2
json_data=requests.get(api_address).json()

def temp():
    temperature = round(json_data["main"]["temp"] - 273,1)
    return temperature

def des():
    description = json_data["weather"][0]["description"]
    return description

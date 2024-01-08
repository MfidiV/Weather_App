import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')

@dataclass
class WeatherData:
    main:str
    description:str
    icon:str
    temperature:int

def get_lan_lon(city_name, state_code, country_code, API_key):
    res = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    data =res[0]
    lat,lon =data.get('lat'),data.get('lon')
    # state = data.get('state'),check other values for state
    return lat,lon

def get_current_weather(lat, lon, API_key):
    res = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
    ).json()
    data = WeatherData(
        main = res.get('weather')[0].get('main'),
        description= res.get('weather')[0].get('description'),
        icon=res.get('weather')[0].get('icon'),
        temperature=int(res.get('main').get('temp'))
    )
    return data
    
def main(city_name,state_name,country_name):
    lat, lon = get_lan_lon(city_name,state_name,country_name, api_key)
    weather_data =get_current_weather(lat,lon,api_key)
    return weather_data


if __name__ == "__main__":
    # Call the get_lan_lon function to get lat and lon values
    lat, lon = get_lan_lon('Toronto', 'ON', 'Canada', api_key)
    # Pass the correct lat, lon, and api_key to get_current_weather
    print(get_current_weather(lat, lon, api_key))
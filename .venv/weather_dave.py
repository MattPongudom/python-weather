# import requests
# from dotenv import load_dotenv
# import os
# from pprint import pprint
#
# load_dotenv()
#
# def get_current_weather():
#     print('\n*** Get Current Weather Condition ***\n')
#
#     city = input("\nPlease input the city name:\n")
#
#     request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEYS")}&q={city}&units=metric'
#     # print(request_url)
#     weather_data = requests.get(request_url).json()
#     pprint(weather_data)
#
#     print(f'\nCurrent weather for {weather_data["name"]}')
#     print(f'\nThe temp is {weather_data["main"]["temp"]} Celsius.')
#     print(f'\nFeels like {weather_data["main"]["feels_like"]} Celsius and {weather_data["weather"][0]["description"]}.')
#
#
# if __name__ == "__main__":
#     get_current_weather()

from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Bangkok"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEYS")}&q={city}&units=metric'
    weather_data = requests.get(request_url).json()
    return weather_data


if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name:\n")
    weather_data = get_current_weather(city)

    # check strings with empty spaces or strings with only spaces
    if not bool(city.strip()):
        city = "Bangkok"

    pprint("\n")
    pprint(weather_data)

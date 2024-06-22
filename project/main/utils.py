

import requests
from django.conf import settings

def get_weather():
    api_key = settings.OPENWEATHERMAP_API_KEY
    location = 'Seoul,KR'  # 서울의 날씨를 가져옵니다. 
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'

    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    weather_main_map = {
        'Clear': '맑음',
        'Clouds': '구름낌',
        'Rain': '비',
        'Snow': '눈',
        'Mist': '흐림',
        'Smoke': '흐림',
        'Haze': '흐림',
        'Dust': '흐림',
        'Fog': '흐림',
        'Sand': '흐림',
        'Ash': '흐림',
        'Squall': '흐림',
        'Drizzle': '비',
        'Thunderstorm': '비',
        'Tornado': '비'
    }

    if weather_response.status_code == 200:
        weather_main = weather_data['weather'][0]['main']
        weather_main_korean = weather_main_map.get(weather_main, 'Unknown')
    else:
        weather_main_korean = 'Unknown'

    return weather_main_korean

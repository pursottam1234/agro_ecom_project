import requests
from django.conf import settings
from django.shortcuts import render

def get_location_key(city, api_key):
    url = f'http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={city}'
    response = requests.get(url)
    data = response.json()
    if data and isinstance(data, list) and len(data) > 0:
        location_key = data[0].get('Key', None)
        return location_key
    return None

def get_weather_data(location_key, api_key):
    url = f'http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}'
    response = requests.get(url)
    return response.json()

def weather_view(request):
    api_key = settings.API_KEY
    locations = ['Kathmandu', 'Pokhara']  # Add more locations as needed

    weather_data = []
    for city in locations:
        location_key = get_location_key(city, api_key)
        if location_key:
            data = get_weather_data(location_key, api_key)
            if data and isinstance(data, list) and len(data) > 0:
                weather = {
                    'name': city,
                    'temperature': data[0]['Temperature']['Metric']['Value'],
                    'description': data[0]['WeatherText'],
                    'icon': data[0]['WeatherIcon'],
                }
                weather_data.append(weather)

    return render(request, 'weather/weather.html', {'weather_data': weather_data})

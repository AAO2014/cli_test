import json
import sys

import requests


def get_weather(city):
    response = requests.get(
        'https://www.metaweather.com/api/location/search/'
        '?query={}'.format(city)
    )
    city_code = json.loads(response.text)[0]['woeid']

    response = requests.get(
        'http://www.metaweather.com/api/location/{}/'.format(city_code)
    )
    result = json.loads(response.text)['consolidated_weather']
    return 'Temperature in {}: {}..{} `C'.format(
        city.f, result[0]['min_temp'], result[0]['max_temp']
    )


if __name__ == "__main__":
    print(get_weather(sys.argv[1]))
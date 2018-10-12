import json
import sys

import requests


def get_weather(city):
    response = requests.get(
        'https://www.metaweather.com/api/location/search/?query={}'.format(city)
    )
    city_code = json.loads(response.text)[0]['woeid']

    response = requests.get(
        'http://www.metaweather.com/api/location/{}/'.format(city_code)
    )
    return json.loads(response.text)['consolidated_weather']


if __name__ == "__main__":
    print(get_weather(sys.argv[1]))
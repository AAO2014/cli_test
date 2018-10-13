import httpretty
import pytest
import requests

from .weather import get_weather


def test_get_weather():
    httpretty.enable()

    httpretty.register_uri(
        httpretty.GET,
        "https://www.metaweather.com/api/location/search/?query=moscow",
        body='[{"woeid": 2122265}]'
    )
    httpretty.register_uri(
        httpretty.GET,
        "https://www.metaweather.com/api/location/2122265/",
        body='{"consolidated_weather":[{"min_temp":0,"max_temp":1}]}'
    )

    result = get_weather('moscow')
    assert result[:14] == 'Temperature in'

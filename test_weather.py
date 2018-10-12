import pytest

from weather import get_weather


def test_ok_responce():
    result = get_weather('moscow')
    assert 'applicable_date' in result[0].keys()
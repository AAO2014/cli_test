#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cmd
import json
import os
import pytest
import requests


class Cli(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "> "
        self.intro  = "Добро пожаловать\nДля справки наберите 'help'"
        self.doc_header ="Доступные команды (для справки по конкретной команде наберите 'help _команда_')"

    def do_show_cpu(self, args):
        """show_cpu - нагрузка на процессоры"""
        os.system("sar 2")

    def do_show_mem(self, args):
        """show_mem - использование RAM"""
        os.system("free")

    def do_show_disk(self, args):
        """show_disk - свободное место на диске"""
        os.system("df -h")

    def do_show_net(self, args):
        """show_net - сетевые параметры"""
        os.system("/sbin/ifconfig")
        os.system("/sbin/route -n")

    def do_show_log(self, args):
        """show_log - системный журнал"""
        os.system("sudo tail -f /var/log/messages")

    def default(self, line):
        print("Несуществующая команда")

    def emptyline(self):
        pass

    def do_show_moscow_weather(self, args):
        """show weather in Moscow"""
        response = requests.get('http://www.metaweather.com/api/location/2122265/')
        print(json.loads(response.text)['consolidated_weather'])

if __name__ == "__main__":
    cli = Cli()
    try:
        cli.cmdloop()
    except KeyboardInterrupt:
        print("завершение сеанса...")




{'title': 'Moscow', 'time': '2018-10-12T21:51:37.916495+03:00',
 'timezone': 'Europe/Moscow', 'latt_long': '55.756950,37.614971',
 'sources': [
    {'title': 'BBC', 'crawl_rate': 180, 'slug': 'bbc',
     'url': 'http://www.bbc.co.uk/weather/'},
    {'title': 'Forecast.io', 'crawl_rate': 480, 'slug': 'forecast-io',
     'url': 'http://forecast.io/'},
    {'title': 'HAMweather', 'crawl_rate': 360, 'slug': 'hamweather',
     'url': 'http://www.hamweather.com/'},
    {'title': 'Met Office', 'crawl_rate': 180, 'slug': 'met-office',
     'url': 'http://www.metoffice.gov.uk/'},
    {'title': 'OpenWeatherMap', 'crawl_rate': 360, 'slug': 'openweathermap',
     'url': 'http://openweathermap.org/'},
    {'title': 'Weather Underground', 'crawl_rate': 720, 'slug': 'wunderground',
     'url': 'https://www.wunderground.com/?apiref=fc30dc3cd224e19b'},
    {'title': 'World Weather Online', 'crawl_rate': 360,
     'slug': 'world-weather-online',
     'url': 'http://www.worldweatheronline.com/'},
    {'title': 'Yahoo', 'crawl_rate': 180, 'slug': 'yahoo',
     'url': 'http://weather.yahoo.com/'}
 ],
 'consolidated_weather': [
    {'applicable_date': '2018-10-12', 'air_pressure': 1030.635,
     'id': 6616742205849600, 'max_temp': 15.2675,
     'wind_speed': 6.704766698083194, 'wind_direction': 272.0,
     'predictability': 70, 'wind_direction_compass': 'W',
     'weather_state_abbr': 'lc', 'visibility': 15.78562445319335,
     'created': '2018-10-12T18:07:38.267120Z', 'humidity': 62,
     'min_temp': 4.625, 'the_temp': 14.575,
     'weather_state_name': 'Light Cloud'},
    {'applicable_date': '2018-10-13', 'air_pressure': 1025.635,
     'id': 4728486073729024, 'max_temp': 15.3275,
     'wind_speed': 6.26220316589716, 'wind_direction': 287.9088581337887,
     'predictability': 71, 'wind_direction_compass': 'WNW',
     'weather_state_abbr': 'hc', 'visibility': 12.117359619820249,
     'created': '2018-10-12T18:07:40.889226Z', 'humidity': 79,
     'min_temp': 7.9275, 'the_temp': 12.315,
     'weather_state_name': 'Heavy Cloud'},
    {'applicable_date': '2018-10-14', 'air_pressure': 1023.135,
     'id': 6597525347762176, 'max_temp': 15.67,
     'wind_speed': 4.722687846118667, 'wind_direction': 301.11201868490883,
     'predictability': 73, 'wind_direction_compass': 'WNW',
     'weather_state_abbr': 's', 'visibility': 11.780265748031496,
     'created': '2018-10-12T18:07:43.884815Z', 'humidity': 82,
     'min_temp': 8.442499999999999, 'the_temp': 12.955,
     'weather_state_name': 'Showers'},
    {'applicable_date': '2018-10-15', 'air_pressure': 1021.7950000000001,
     'id': 4922259529531392, 'max_temp': 17.0975,
     'wind_speed': 4.255170578604947, 'wind_direction': 297.0819021236104,
     'predictability': 68, 'wind_direction_compass': 'WNW',
     'weather_state_abbr': 'c', 'visibility': 14.239342241310744,
     'created': '2018-10-12T18:07:47.550729Z', 'humidity': 77,
     'min_temp': 6.8925, 'the_temp': 14.815, 'weather_state_name': 'Clear'},
    {'applicable_date': '2018-10-16', 'air_pressure': 1017.69,
     'id': 5323451384463360, 'max_temp': 15.7025,
     'wind_speed': 5.810130255869721, 'wind_direction': 250.78902725309842,
     'predictability': 70, 'wind_direction_compass': 'WSW',
     'weather_state_abbr': 'lc', 'visibility': 14.381014873140858,
     'created': '2018-10-12T18:07:49.861228Z', 'humidity': 71,
     'min_temp': 6.01, 'the_temp': 15.620000000000001,
     'weather_state_name': 'Light Cloud'},
    {'applicable_date': '2018-10-17', 'air_pressure': 1006.43,
     'id': 6542363572830208, 'max_temp': 13.8425,
     'wind_speed': 4.957659004745619, 'wind_direction': 257.41335724768584,
     'predictability': 70, 'wind_direction_compass': 'WSW',
     'weather_state_abbr': 'lc', 'visibility': 9.997862483098704,
     'created': '2018-10-12T18:07:54.052794Z', 'humidity': 73,
     'min_temp': 6.1125, 'the_temp': 15.08,
     'weather_state_name': 'Light Cloud'}],
 'sun_set': '2018-10-12T17:37:19.542480+03:00', 'timezone_name': 'LMT',
 'location_type': 'City', 'woeid': 2122265,
 'sun_rise': '2018-10-12T06:53:46.859119+03:00',
 'parent': {'title': 'Russia', 'woeid': 23424936, 'location_type': 'Country',
            'latt_long': '59.453751,108.830719'}}

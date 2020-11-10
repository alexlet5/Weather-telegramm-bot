import pyowm
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM('e72fa5cda4b9c1084641774fac39d7cd', config_dict)


def get_citys_list(place):
    mgr = owm.weather_manager()
    return mgr.weather_at_places(place, 'accurate')


def get_city_info(places_list, place):
    weather = places_list[0].weather
    temp_dict_celsius = weather.temperature('celsius')
    city_info = "В городе " + place + " сейчас " + str(weather.detailed_status)
    temp_info = " Температура = " + \
        str(temp_dict_celsius['temp']) + ", но ощущается на = " + \
        str(temp_dict_celsius['feels_like'])
    info = city_info + temp_info
    return info


if __name__ == '__main__':
    place = input("Какой город?: ")
    places_list = get_citys_list(place)
    print(get_city_info(places_list, place))

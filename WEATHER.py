import json
from typing import Union

import requests

URL = 'https://api.m3o.com/v1/weather/'
HEADERS = {'Content-Type': 'application/json',
           'Authorization': 'Bearer ZjI3ZTk3NmYtMDk3NS00Y2IyLTk1NWEtNzg0NmNkNGE3ODE3'}


def display_result_on_screen(weather_forecast: Union[dict, None]) -> None:
    """
    Visualizes the result
    """

    if weather_forecast is not None:
        counter = 1
        print(f"\nПрогноз погоды для города: {weather_forecast['response_location']}")
        for k, v in weather_forecast['list_dates'].items():
            if v > 0:
                v = '+' + str(v)
            if counter == 1:
                print(f'Температура сегодня, {k.split()[0]}: {v} градус(а/ов)')
            elif counter == 2:
                print(f'Температура завтра, {k.split()[0]}: {v} градус(а/ов)')
            else:
                print(f'Температура {k.split()[0]}: {v} градус(а/ов)')
            counter += 1

    else:
        print('\nЧто-то пошло не так...')


def receive_users_request() -> tuple[dict, None]:
    """
    Gets the request mode from the user
    """

    users_request = input('''Выберите режим (нажмите 1 или 2):
1. Текущая погода
2. Прогноз погоды (до 10 дней)
''')
    if users_request == '1' or users_request == '2':
        return launch_mode(users_request)
    else:
        print('\nОшибка! Попробуйте еще раз \n')
        receive_users_request()


def ask_location_weather_forecast() -> str:
    """
    Gets the name of the city from the user
    """

    location = input('''\nУкажите город определения прогноза погоды.
Например Moscow, London... Tokyo
''')
    return location.title().strip()


def launch_mode(users_request: str) -> tuple[dict, None]:
    """
    Makes an object of the Weather Forecast class for the future or for today (now)
    Receive the name of the city from the user
    Returns the result of accessing the weather API
    """

    if users_request == '1':
        processor = WeatherNow()
    else:
        processor = WeatherForecast()
    location = ask_location_weather_forecast()
    return processor.processes_weather_request(location)


class WeatherNow:
    def processes_weather_request(self, location: str) -> tuple[dict, None]:
        """
        Requests the weather API and generates a DTO
        """

        RESULT, LIST_DATES = {}, {}

        try:
            response = requests.post(URL + 'Now', headers=HEADERS, data=json.dumps({"location": f"{location}"}))
        except:
            return None

        try:
            RESULT['response_location'] = response.json()['location']
            LIST_DATES[response.json()['local_time']] = response.json()['temp_c']
            RESULT['list_dates'] = LIST_DATES
        except:
            RESULT = None

        return RESULT


class WeatherForecast:
    def processes_weather_request(self, location: str) -> tuple[dict, None]:
        """
        Receive the amount weather forecast days from the user
        Requests the weather API and generates a DTO
        """

        RESULT, LIST_DATES = {}, {}
        amo_days = self.__days_delta()

        try:
            response = requests.post(URL + 'Forecast', headers=HEADERS,
                                     data=json.dumps({"days": amo_days, "location": f"{location}"}))
        except:
            return None

        try:
            RESULT['response_location'] = response.json()['location']

            for day_info in response.json()['forecast']:
                LIST_DATES[day_info['date']] = day_info['max_temp_c']

            RESULT['list_dates'] = LIST_DATES
        except:
            RESULT = None

        return RESULT

    def __days_delta(self) -> int:
        """
        Gets the amount weather forecast days from the user
        """

        self.users_days_delta = input(
            '\nНа сколько дней вы бы хотели получить прогноз погоды (от 1 до 10 (включительно))? \n')

        try:
            self.users_days_delta = int(self.users_days_delta)
        except:
            print('Вы ввели не число. Попробуйте еще раз \n')
            self.__days_delta()

        if self.users_days_delta < 1 or self.users_days_delta > 10:
            print('Ошибка! Введите число от 1 до 10 \n')
            self.__days_delta()
        return self.users_days_delta


if __name__ == "__main__":
    weather_forecast = receive_users_request()

    # To visualize the display, comment out the line below
    # display_result_on_screen(weather_forecast)

import requests
import os
from dotenv import find_dotenv, load_dotenv
import logging

logger = logging.getLogger(__name__)

load_dotenv(find_dotenv())

class WeatherAPIConn:
    def __init__(self, API_KEY=os.getenv('API_KEY'), API_URL=os.getenv('API_URL'),location='264879'):
        self.apiurl = API_URL,
        self.apikey = API_KEY,
        self.location = location,
        self.params = {'apikey': self.apikey}
        self.session = requests.Session()

    def get_daily_forecast(self) -> dict:
        """
        Retrieves the daily forecast from the API.

        :return: A dictionary containing the daily forecast.
        :rtype: dict
        """
        try:
            logger.info('Getting daily forecast...')
            url = f'{self.apiurl[0]}/daily/5day/{self.location[0]}/'
            response = requests.get(url, params=self.params)
            response.raise_for_status()
            logger.info('Daily forecast retrieved.')
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f'Error retrieving daily forecast: {e}')
            raise e



    def get_hourly_forecast(self) -> dict:
        """
        Retrieves the hourly forecast from the API.

        :return: A dictionary containing the hourly forecast data.
        :rtype: dict
        """
        try:
            logger.info('Getting hourly forecast...')
            url = f'{self.apiurl[0]}/hourly/12hour/{self.location[0]}/'
            response = requests.get(url, params=self.params)
            response.raise_for_status()
            logger.info('Hourly forecast retrieved.')
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f'Error retrieving hourly forecast: {e}')
            raise e


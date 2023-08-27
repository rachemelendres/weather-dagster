import requests
from requests import Session
import os
from dotenv import find_dotenv, load_dotenv
import json
import logging

logger = logging.getLogger(__name__)

load_dotenv(find_dotenv())

API_KEY = os.getenv('API_KEY')

class APIConnection:
    def __init__(self, key=API_KEY):
        self.apiurl = 'http://dataservice.accuweather.com/forecasts/v1'
        self.apikey = key
        self.params = {'apikey': self.apikey}
        self.session = Session()

    def getDailyForecast(self) -> dict:
        """
        Retrieves the daily forecast from the API.

        :param self: The instance of the class.
        :return: A dictionary containing the daily forecast.
        :rtype: dict
        """
        logger.info('Getting daily forecast...')
        url = f'{self.apiurl}/daily/5day/264879/'
        response = self.session.get(url, params=self.params)
        logger.info('Daily forecast retrieved.')
        return response.json()

    def getHourlyForecast(self) -> dict:
        """
        Retrieves the hourly forecast from the API.

        :return: A dictionary containing the hourly forecast data.
        :rtype: dict
        """
        logger.info('Getting hourly forecast...')
        url = f'{self.apiurl}/hourly/12hour/264879/'
        response = self.session.get(url, params=self.params)
        logger.info('Hourly forecast retrieved.')
        return response.json()



from dagster import Definitions
from dagster import load_assets_from_modules
from src.assets import forecast_dag
from src.resources.weather_resource import WeatherAPIConn
import os
import requests
import json
forecast_assets = load_assets_from_modules([forecast_dag])
API_URL = os.getenv('API_URL')
API_KEY = os.getenv('API_KEY')

defs = Definitions(assets=[*forecast_assets])
import os
from src.utils.api_conn import WeatherAPIConn
from src.daily_forecast import parse_daily_forecast, write_daily_forecast_to_csv
from src.hourly_forecast import parse_hourly_forecast,write_hourly_forecast_to_csv
import logging
import sys
import datetime
from dagster import asset, op, AssetIn, OpExecutionContext
from src.resources.weather_resource import WeatherAPIConn




def setup_logging():
    LOG_DIR = os.path.join(os.getcwd(), 'logs')
    log_filepath = os.path.join(LOG_DIR,f'{datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")}.app.log')

    logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
            logging.FileHandler(log_filepath),
            logging.StreamHandler()
        ]
    )

@asset(description='Initialize API connection',
       group_name='api')
def init_api_conn():
    setup_logging()
    logger = logging.getLogger(__name__)
    api_conn = WeatherAPIConn()
    
    return api_conn

@asset(group_name='daily_forecast',
       description='Get daily forecast data',
       ins={'api_conn': AssetIn('init_api_conn')})
def get_daily_forecast_data(api_conn) -> dict:
    daily_data_dict = api_conn.get_daily_forecast()
    return daily_data_dict


@asset( group_name='daily_forecast',
       description='Parse daily forecast data',
        ins={'daily_data_dict': AssetIn('get_daily_forecast_data')}
        )
def parse_daily_forecast_data(daily_data_dict) -> dict:
    parsed_daily_data = parse_daily_forecast(daily_data_dict)
    return parsed_daily_data

@asset(group_name='daily_forecast',
       description='Write daily forecast data to CSV',
        ins={'parsed_daily_data': AssetIn('parse_daily_forecast_data')})
def write_daily_forecast_data(parsed_daily_data) -> None:
    DATA_DIR = os.path.join(os.getcwd(), 'data')
    write_daily_forecast_to_csv(parsed_daily_data, DATA_DIR)
    
@asset(group_name='hourly_forecast',
       description='Get hourly forecast data',
       ins={'api_conn': AssetIn('init_api_conn')})
def get_hourly_forecast_data(api_conn) -> dict:
    hourly_data_dict = api_conn.get_hourly_forecast()
    return hourly_data_dict


@asset( group_name='hourly_forecast',
       description='Parse hourly forecast data',
        ins={'hourly_data_dict': AssetIn('get_hourly_forecast_data')}
        )
def parse_hourly_forecast_data(hourly_data_dict) -> dict:
    parsed_hourly_data = parse_hourly_forecast(hourly_data_dict)
    return parsed_hourly_data

@asset(group_name='hourly_forecast',
       description='Write hourly forecast data to CSV',
        ins={'parsed_hourly_data': AssetIn('parse_hourly_forecast_data')})
def write_hourly_forecast_data(parsed_hourly_data) -> None:
    DATA_DIR = os.path.join(os.getcwd(), 'data')
    write_hourly_forecast_to_csv(parsed_hourly_data, DATA_DIR)


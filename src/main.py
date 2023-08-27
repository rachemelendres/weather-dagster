import os
from utils.api_conn import WeatherAPIConn
from daily_forecast import parse_daily_forecast, write_daily_forecast_to_csv
from hourly_forecast import parse_hourly_forecast,write_hourly_forecast_to_csv
import logging
import sys
import datetime
from dagster import asset

DATA_DIR = os.path.join(os.getcwd(), 'data')

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





def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    try:
        logger.info('Program started')
        # Create an instance of the Weather API connection
        api_conn = WeatherAPIConn()

        # Retrieve daily and hourly forecast data from the API
        daily_data_dict = api_conn.get_daily_forecast()
        hourly_data_dict = api_conn.get_hourly_forecast()

        # Parse the daily and hourly forecast data
        parsed_daily_data = parse_daily_forecast(daily_data_dict)
        parsed_hourly_data = parse_hourly_forecast(hourly_data_dict)

        # Save parsed daily and hourly forecast data to a CSV file
        write_daily_forecast_to_csv(parsed_daily_data, DATA_DIR)
        write_hourly_forecast_to_csv(parsed_hourly_data, DATA_DIR)
        
        logger.info('Program completed')
    except Exception as e:
        logger.exception('An error occurred while attempting to start the program.')
        raise e
    
if __name__ == "__main__":
    main()

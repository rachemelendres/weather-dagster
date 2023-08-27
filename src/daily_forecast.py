import os
import csv
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def parse_daily_forecast(daily_forecast_dict) -> dict:
    """
    Parses the daily forecast data from a dictionary and returns a parsed version.

    Args:
        daily_forecast_dict (dict): A dictionary containing the daily forecast data.

    Returns:
        dict: A dictionary with the parsed daily forecast data. The keys are the following:
            - 'Date': A list of dates for each forecast.
            - 'Min Temperature': A list of minimum temperatures for each forecast.
            - 'Max Temperature': A list of maximum temperatures for each forecast.
            - 'Day Icon Phrase': A list of icon phrases for the day forecast.
            - 'Day Has Precipitation': A list indicating if there is precipitation during the day.
            - 'Day Precipitation Type': A list of precipitation types during the day.
            - 'Day Precipitation Intensity': A list of precipitation intensities during the day.
            - 'Night Icon Phrase': A list of icon phrases for the night forecast.
            - 'Night Has Precipitation': A list indicating if there is precipitation during the night.
            - 'Night Precipitation Type': A list of precipitation types during the night.
            - 'Night Precipitation Intensity': A list of precipitation intensities during the night.
    """
    try:
        logger.info('Parsing daily forecast...')
        daily_forecasts = daily_forecast_dict.get('DailyForecasts', [])

        headers = [
            'Date',
            'Min Temperature',
            'Max Temperature',
            'Day Icon Phrase',
            'Day Has Precipitation',
            'Day Precipitation Type',
            'Day Precipitation Intensity',
            'Night Icon Phrase',
            'Night Has Precipitation',
            'Night Precipitation Type',
            'Night Precipitation Intensity'
        ]

        parsed_daily_forecast_data = {header: [] for header in headers}

        for forecast in daily_forecasts:
            parsed_daily_forecast_data['Date'].append(forecast.get('Date', ''))
            parsed_daily_forecast_data['Min Temperature'].append(forecast['Temperature']['Minimum'].get('Value', ''))
            parsed_daily_forecast_data['Max Temperature'].append(forecast['Temperature']['Maximum'].get('Value', ''))
            parsed_daily_forecast_data['Day Icon Phrase'].append(forecast['Day'].get('IconPhrase', ''))
            parsed_daily_forecast_data['Day Has Precipitation'].append(forecast['Day'].get('HasPrecipitation', ''))
            parsed_daily_forecast_data['Day Precipitation Type'].append(forecast['Day'].get('PrecipitationType', ''))
            parsed_daily_forecast_data['Day Precipitation Intensity'].append(forecast['Day'].get('PrecipitationIntensity', ''))
            parsed_daily_forecast_data['Night Icon Phrase'].append(forecast['Night'].get('IconPhrase', ''))
            parsed_daily_forecast_data['Night Has Precipitation'].append(forecast['Night'].get('HasPrecipitation', ''))
            parsed_daily_forecast_data['Night Precipitation Type'].append(forecast['Night'].get('PrecipitationType', ''))
            parsed_daily_forecast_data['Night Precipitation Intensity'].append(forecast['Night'].get('PrecipitationIntensity', ''))
        logger.info('Daily forecast parsed.')
        return parsed_daily_forecast_data
    except Exception as e:
        logger.exception('Error parsing daily forecast.')
        raise e
def write_daily_forecast_to_csv(data, data_filepath) -> None:
    """
    Write daily forecast data to a CSV file.

    Parameters:
        data (dict): A dictionary containing the forecast data.
        data_filepath (str): The file path where the CSV file will be written.

    Returns:
        None
    """
    try:
        logger.info('Writing daily forecast data to CSV file...')
        headers = list(data.keys())
        rows = zip(*data.values())
        
        current_datetime = datetime.now().strftime('%Y-%m-%d-%H%M%S')
        filename = f'{current_datetime}_daily_forecast.csv'
        DAILY_FORECAST_FILEPATH = os.path.join(data_filepath, filename)

        with open(DAILY_FORECAST_FILEPATH, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(rows)
        logger.info('Daily forecast data written to CSV file.')
    except Exception as e:
        logger.exception('Error writing daily forecast data to CSV file.')
        raise e

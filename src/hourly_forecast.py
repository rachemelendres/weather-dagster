import os
import csv
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def parse_hourly_forecast(hourly_forecast_dict: dict) -> dict:
    """
    Parses the hourly forecast data from the given `hourly_forecast_dict` and returns a dictionary of parsed data.

    Parameters:
        - hourly_forecast_dict (dict): A dictionary containing the hourly forecast data.

    Returns:
        - dict: A dictionary containing the parsed hourly forecast data.

    """  
    try:
        logger.info('Parsing daily forecast...')
        # hourly_forecasts = hourly_forecast_dict.get('HourlyForecasts', [])

        headers = [
            'DateTime',
            'EpochDateTime',
            'WeatherIcon',
            "IconPhrase",
            "HasPrecipitation",
            "PrecipitationType",
            "PrecipitationIntensity",
            "IsDaylight",
            "Temperature.Value",
            "Temperature.Unit",
            "Temperature.UnitType"

        ]

        parsed_hourly_forecast_data = {header: [] for header in headers}

        for forecast in hourly_forecast_dict:
            parsed_hourly_forecast_data['DateTime'].append(forecast.get('DateTime', ''))
            parsed_hourly_forecast_data['EpochDateTime'].append(forecast.get('EpochDateTime', ''))
            parsed_hourly_forecast_data['WeatherIcon'].append(forecast.get('WeatherIcon', ''))
            parsed_hourly_forecast_data['IconPhrase'].append(forecast.get('IconPhrase', ''))
            parsed_hourly_forecast_data['HasPrecipitation'].append(forecast.get('HasPrecipitation', ''))
            parsed_hourly_forecast_data['PrecipitationType'].append(forecast.get('PrecipitationType', ''))
            parsed_hourly_forecast_data['PrecipitationIntensity'].append(forecast.get('PrecipitationIntensity', ''))
            parsed_hourly_forecast_data['IsDaylight'].append(forecast.get('IsDaylight', ''))
            parsed_hourly_forecast_data['Temperature.Value'].append(forecast['Temperature'].get('Value', ''))
            parsed_hourly_forecast_data['Temperature.Unit'].append(forecast['Temperature'].get('Unit', ''))
            parsed_hourly_forecast_data['Temperature.UnitType'].append(forecast['Temperature'].get('UnitType', ''))
        logger.info('Hourly forecast parsed.')
        return parsed_hourly_forecast_data
    except Exception as e:
        logger.exception('Error parsing hourly forecast data.')
        raise e
def write_hourly_forecast_to_csv(data :dict, data_filepath) -> None:
    """
    Write hourly forecast data to a CSV file.

    Args:
        data (dict): A dictionary containing the hourly forecast data. The keys represent the headers of the CSV file, and the values are the corresponding data rows.
        data_filepath (str): The path to the directory where the CSV file will be saved.

    Returns:
        None

    Raises:
        None
    """

    try:
        logger.info('Writing hourly forecast data to CSV file...')
        headers = list(data.keys())
        rows = zip(*data.values())
        
        current_datetime = datetime.now().strftime('%Y-%m-%d-%H%M%S')
        filename = f'{current_datetime}_hourly_forecast.csv'
        HOURLY_FORECAST_FILEPATH = os.path.join(data_filepath, filename)

        with open(HOURLY_FORECAST_FILEPATH, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            writer.writerows(rows)
        logger.info('Hourly forecast data written to CSV file.')
    except Exception as e:
        logger.exception('Error writing hourly forecast data to CSV file.')
        raise e
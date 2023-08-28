
from dagster import Definitions
from dagster import load_assets_from_modules
from src.assets import forecast_dag
from src.resources.weather_resource import WeatherAPIConn
from src.jobs import daily_forecast_job, hourly_forecast_job, api_client_job
from src.schedules import api_client_schedule, daily_forecast_schedule, hourly_forecast_schedule



forecast_assets = load_assets_from_modules([forecast_dag])
all_jobs = [daily_forecast_job, hourly_forecast_job, api_client_job]
all_schedules = [api_client_schedule, daily_forecast_schedule, hourly_forecast_schedule]
defs = Definitions(assets=[*forecast_assets], jobs=all_jobs, schedules=all_schedules)
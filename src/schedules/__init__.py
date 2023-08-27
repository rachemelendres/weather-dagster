from dagster import ScheduleDefinition
from src.jobs import daily_forecast_job, hourly_forecast_job, api_client_job

api_client_schedule = ScheduleDefinition(
    job=api_client_job,
    cron_schedule="0 12 * * *", # every 12th of the month at midnight
)

daily_forecast_schedule = ScheduleDefinition(
    job=daily_forecast_job,
    cron_schedule="0 12 * * *", 

)

hourly_forecast_schedule = ScheduleDefinition(
    job=hourly_forecast_job,
    cron_schedule="0 0 1 * *",
    
    )
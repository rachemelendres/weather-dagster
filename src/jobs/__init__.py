from dagster import AssetSelection, define_asset_job

daily_forecast_asset= AssetSelection.groups('daily_forecast')

daily_forecast_job = define_asset_job(
    name="daily_forecast_job",
    selection=daily_forecast_asset
)

hourly_forecast_asset= AssetSelection.groups('hourly_forecast')


hourly_forecast_job = define_asset_job(name="hourly_forecast_job",
    selection=hourly_forecast_asset
)

api_client= AssetSelection.groups('api')


api_job = define_asset_job(name="api_job",
    selection=hourly_forecast_asset
)
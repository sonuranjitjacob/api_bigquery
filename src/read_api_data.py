import requests
import logging
from datetime import datetime, timedelta
from utils.utils import send_api_get_request

def read_weatherapi_history_data(url):

    """  
    This function sends a GET request to the specified URL to retrieve
    historical weather data by the hour. It logs a success message upon
    successful retrieval.

    Parameters:
    - url (str): The URL of the API endpoint for historical weather data.

    Returns:
    dict: A dictionary containing historical weather data by the hour.
    """

    # Send a GET request to retrieve the historical weather data
    weather_data_by_hour = send_api_get_request(url)
    logging.info(f"Data retrieved successfully")

    return weather_data_by_hour

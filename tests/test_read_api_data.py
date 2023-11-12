
import requests
import pytest
from src.read_api_data import read_weatherapi_history_data


# Test for a successful API request
def test_successful_api_request(api_base_url):
    response = requests.get(api_base_url)
    assert response.status_code == 200
   
# Test if expected fields are present in the API response
def test_read_weatherapi_history_data_success(api_base_url):
    response = read_weatherapi_history_data(api_base_url) 
    assert "location" in response.keys()
    assert "forecast" in response.keys()
    assert "forecastday" in response["forecast"].keys()
    assert "hour" in response["forecast"]["forecastday"][0]



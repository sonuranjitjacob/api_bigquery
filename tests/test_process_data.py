import pytest
from src.process_data import process_weatherapi_history_data
from src.read_api_data import read_weatherapi_history_data


# Test if the processed data has expected number of rows
def test_process_weatherapi_history_data_success(api_base_url):
    response = read_weatherapi_history_data(api_base_url)
    transformed_data = process_weatherapi_history_data(response)
    assert len(transformed_data) == 24

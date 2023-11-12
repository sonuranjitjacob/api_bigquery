import pytest
from utils.utils import load_config
import os

config_file = 'config/config.yaml'
config = load_config(config_file)

# Define a fixture to set up the API base URL
@pytest.fixture
def api_base_url():    
    url = config.get('api_url')
    return url  

# Define a fixture to get the service account file name
@pytest.fixture
def service_account_file_path():
    service_account_file_name = config.get('service_account_file_name')
    service_account_file_name_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'service_account_key', f'{service_account_file_name}'))
    return service_account_file_name_path  

#Define a fixture to get the dataset name
@pytest.fixture
def dataset_name():
    dataset_name = config.get('dataset_name')
    return dataset_name  

#Define a fixture to get the table name
@pytest.fixture
def table_name():
    table_name = config.get('table_name')
    return table_name  
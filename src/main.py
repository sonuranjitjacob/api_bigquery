import os
import logging
from read_api_data import read_weatherapi_history_data
from process_data import process_weatherapi_history_data
from write_data_to_bigquery import write_data_to_bigquery
from utils.utils import load_config

# Configure logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Main function to retrieve weather data from an API, preprocess it, and store it in BigQuery.

    This script retrieves weather data from an API using an API key stored in a .env file,
    preprocesses the data, and stores it in a specified BigQuery dataset and table.

    """

    config_file_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml'))
    config = load_config(config_file_path)


    service_account_file_name = config.get('service_account_file_name')
    # Define BigQuery credentials and project details
    service_account_key_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'service_account_key', f'{service_account_file_name}'))

    project_id = config.get('project_name')
    dataset_id = config.get('dataset_name')
    table_id = config.get('table_name')

    api_url = config.get('api_url')

    # Read data from the weather API
    logging.info(f"Reading data from weather API............")
    weather_data_by_hour = read_weatherapi_history_data(api_url)

    # Preprocess the retrieved data
    logging.info(f"Processing weather API data............")
    cleaned_weather_data_by_hour = process_weatherapi_history_data(weather_data_by_hour)

    # Write the preprocessed data to BigQuery dataset
    write_data_to_bigquery(project_id, dataset_id, table_id, service_account_key_path, cleaned_weather_data_by_hour)

if __name__ == "__main__":
    main()

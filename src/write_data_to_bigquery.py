import os
import pandas as pd
from google.cloud import bigquery
import logging

def write_data_to_bigquery(project_id, dataset_id, table_id, service_account_key_path, cleaned_weather_data_by_hour):

    """
    Write cleaned weather data to Google BigQuery. It uses the Google Cloud BigQuery client library
    and requires a service account key for authentication.

    Parameters:
    - project_id (str): The Google Cloud project ID where the BigQuery dataset is located.
    - dataset_id (str): The name of the dataset within the specified project.
    - table_id (str): The name of the BigQuery table to write the data to.
    - service_account_key_path (str): The file path to the service account key JSON file
      for authentication.
    - cleaned_weather_data_by_hour (pd.DataFrame): The Pandas DataFrame containing cleaned
      weather data to be written to BigQuery.

    Returns:
    None
    """

    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Set the path to your service account key JSON file
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_account_key_path

    # Explicitly set the credentials using the key file
    client = bigquery.Client.from_service_account_json(service_account_key_path)

    # Initialize the BigQuery client
    client = bigquery.Client(project=project_id)

    # Define your data in a list of dictionaries
    data = cleaned_weather_data_by_hour

    try:
        # Write the DataFrame to BigQuery
        data.to_gbq(destination_table=f"{project_id}.{dataset_id}.{table_id}", project_id=project_id, if_exists="append")

        logging.info(f"DataFrame written to {project_id}:{dataset_id}.{table_id}")

        logging.info(f"Loaded {len(data)} rows into {project_id}:{dataset_id}.{table_id}")
        
    except Exception as e:
        logging.error(f"An error occurred while writing to BigQuery: {str(e)}")

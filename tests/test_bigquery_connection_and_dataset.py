import pytest
from google.cloud import bigquery
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#Test if the connection to BigQuery is possible and if specified dataset and table exist
def test_bigquery_connection_and_dataset(service_account_file_path, dataset_name, table_name):
    try:
        # Create a BigQuery client with your service account key
        client = bigquery.Client.from_service_account_json(service_account_file_path)

        # List datasets in your BigQuery project 
        datasets = list(client.list_datasets())
        dataset_ids = [dataset.dataset_id for dataset in datasets]
        
        #Check if dataset exists
        assert dataset_name in dataset_ids

        #Check if table exists
        dataset_ref = client.dataset(dataset_name)
        tables = list(client.list_tables(dataset_ref))
        print(f"THE TABLES ARE {tables}")
        table_names = [table.table_id for table in tables]
        assert table_name in table_names

    except Exception as e:
        # Handle any exceptions that may occur during the connection
        pytest.fail(f"Error connecting to BigQuery: {e}")
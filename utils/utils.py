import logging
import yaml
import requests

def load_config(config_file):
    try:
        with open(config_file, 'r') as stream:
            config = yaml.safe_load(stream)
        return config
    except Exception as e:
        logging.error(f"Error loading configuration: {str(e)}")
        return None

def send_api_get_request(url):

    # Send a GET request
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

    else:
        # Handle the error if the request was not successful
        logging.error(f"Error: {response.status_code} - {response.text}")
        data = None

    return data
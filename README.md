# Write API data to Google Bigquery

This repository contains the code to read data from a weather API website, clean and process it and write it to a table in Google Bigquery. It also implements some tests using `pytest`.

### Prerequisites

Requirements for the software and other tools to build, test and push 
- Python (3.8 or higher)
- Docker
- Service account file for a Google Cloud project with the right IAM roles 

### Installation and Setup

1. Clone the repository. Create a virtual environment (preferred) before completing the next steps.

2. To install the required libraries, run the following command in the terminal:

        pip install pandas python-dotenv pandas-gbq google-cloud-bigquery pyyaml pytest

3. Place your service account file in the folder service_account_key
4. Create a config.yaml file and fill in the appropriate values. See [config_sample.yaml](config/config_sample.yaml) 


### Model structure

The code is structured as follows:

   
        docker-compose.yml
        Dockerfile
        README.md
        ├── src                                
            ├── main.py        
            ├── process_data.py    
            ├── read_api_data.py
            ├── write_data_bigquery.py
        ├── utils                                
            ├── utils.py
        ├── config                                
            ├── config.yaml
        ├── tests                         
            ├── conftest.py     
            ├── test_bigquery_connection_and_dataset.py
            ├── test_process_data.py   
            ├── test_read_api_data.py  
        ├── service_account_key   
            ├── your_service_account_file.json
                    

### To run the script and upload data to the BigQuery dataset
cd to the directory src. Run the following command:

        python main.py

### To test the scripts 
Run the following command in the root folder:

        python -m pytest 

### To test the scripts and run it in a Docker container
Run the following command in the root folder:

        docker-compose up --build



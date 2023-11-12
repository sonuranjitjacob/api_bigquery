
FROM python:3.9  

RUN pip install pandas python-dotenv pandas-gbq google-cloud-bigquery pyyaml pytest

WORKDIR /app
COPY . /app

ENV PYTHONPATH /app
RUN ["python", "-m", "pytest"]
RUN ["python", "src/main.py"]
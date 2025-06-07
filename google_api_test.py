import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.cloud import bigquery
from google.cloud import storage
from my_creds import my_creds
my_creds()
client = bigquery.Client()
datasets = client.list_datasets()
for dataset in datasets:
    print(dataset.dataset_id)

query = """
SELECT
    FORMAT_TIMESTAMP("%Y-%m-%d %H:%M:%S %Z", pickup_datetime) AS pickup_datetime,
    pickup_longitude, pickup_latitude, dropoff_longitude,
    dropoff_latitude, passenger_count, trip_distance, tolls_amount, 
    fare_amount, total_amount 
FROM
    `nyc-tlc.yellow.trips`
LIMIT 10
"""
query_job = client.query(query)
results = query_job.result()
df = query_job.to_dataframe()
df

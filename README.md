# Overview
This is a basic POC of data ingestion, cleaning, transformation and statistical analysis of a consumer behavioural dataset. The dataset can be used further to analyze the consumer behaviour and predicts the market trends based on the user behaviour.
# Prerequisites
Before running the DAG, ensure you have the following prerequisites:

1. Apache Airflow installed and configured.
2. Python dependencies installed, including pandas.

# File Structure
1. ETL.py: The main DAG file containing the workflow logic.
2. sample_data_file.csv: Sample CSV file for data ingestion.

# DAG Structure
# Tasks
<b> Data Ingestion (data_ingestion):</b>

1. Reads the CSV data from sample_data_file.csv.
2. Validates the existence of the file before reading.

<b>Data Cleaning (data_cleaning):</b>

1. Removes empty columns.
2. Drops duplicate rows.
3. Normalizes column names.

<b> Transformation (transformation):</b>

1. Applies various transformations to the data:
2. Fills missing numeric values with the mean.
3. Fills missing float values with the mean.
4. Fills missing categorical values with the mode.

<b> Statistical Analysis (statistical_analysis):</b>

1. Computes statistical measures such as mean, median, and standard deviation on the 'age' column.

<b> Save to CSV (save_to_csv):</b>

1. Saves the transformed data to a CSV file named transformed_data.csv.

<b>Workflow</b>

1. The workflow follows the sequence: data_ingestion ➔ data_cleaning ➔ transformation ➔ statistical_analysis ➔ save_to_csv.

# Usage

1. Ensure that Apache Airflow is up and running.

2. Place the CSV file (sample_data_file.csv) in the same directory as ETL.py.

3. Copy the DAG file (ETL.py) to the DAGs directory of your Apache Airflow installation.

4. Access the Airflow web interface and trigger the DAG manually or let it run according to its schedule.

# Note

1. The DAG is configured with schedule_interval=None, indicating it needs to be triggered manually.

2. Adjust the file paths as per your requirements.

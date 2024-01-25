# Overview
# Prerequisites
Before running the DAG, ensure you have the following prerequisites:

Apache Airflow installed and configured.
Python dependencies installed, including pandas.

# File Structure
ETL.py: The main DAG file containing the workflow logic.
sample_data_file.csv: Sample CSV file for data ingestion.

# DAG Structure
# Tasks
<b> Data Ingestion (data_ingestion):</b>

Reads the CSV data from sample_data_file.csv.
Validates the existence of the file before reading.
Data Cleaning (data_cleaning):

Removes empty columns.
Drops duplicate rows.
Normalizes column names.
Transformation (transformation):

Applies various transformations to the data:
Fills missing numeric values with the mean.
Fills missing float values with the mean.
Fills missing categorical values with the mode.
Statistical Analysis (statistical_analysis):

Computes statistical measures such as mean, median, and standard deviation on the 'age' column.
Save to CSV (save_to_csv):

Saves the transformed data to a CSV file named transformed_data.csv.
Workflow
The workflow follows the sequence: data_ingestion ➔ data_cleaning ➔ transformation ➔ statistical_analysis ➔ save_to_csv.

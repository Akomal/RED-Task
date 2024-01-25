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

Computes statistical measures such as mean, median, and standard deviation on the 'age' column.

<b> Save to CSV (save_to_csv):</b>

Saves the transformed data to a CSV file named transformed_data.csv.

<b>Workflow</b>
The workflow follows the sequence: data_ingestion ➔ data_cleaning ➔ transformation ➔ statistical_analysis ➔ save_to_csv.

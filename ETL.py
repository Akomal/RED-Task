from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
import os
import pandas as pd

@dag(schedule_interval=None, start_date=None, catchup=False)
def red_dag():

    @task
    def data_ingestion():
        # Get the directory of the DAG file
        dag_directory = os.path.dirname(os.path.abspath(__file__))

        # Construct the absolute path to the CSV file
        file_path = os.path.join(dag_directory, 'sample_data_file.csv')

        # Check if the file exists before reading it
        if os.path.exists(file_path):
            data = pd.read_csv(file_path)
            return data
        else:
            raise FileNotFoundError(f"File not found: {file_path}")

    @task
    def data_cleaning(data):
       #drop empty columns
        empty_columns = []

        for column in data.columns:
            is_empty = data[column].isna().all()
            if is_empty:
                empty_columns.append(column)

        data.drop(columns=empty_columns, inplace=True)
        #drop duplicates
        data.drop_duplicates(inplace=True)
        #convert the column name to lowercase and remove special characters, numbers
        for column in data.columns:
            data.rename(columns={column: column.lower().replace('[^A-Za-z0-9_]+', '_')}, inplace=True)

        return data

    @task
    def transformation(data):
       #replace the missing numerical values with mean and categorical values with mode
        for col in data.columns:
            if pd.api.types.is_numeric_dtype(data[col]):
                if pd.isnull(data[col]).any():
                    data[col].fillna(data[col].mean(), inplace=True)
            elif pd.api.types.is_float_dtype(data[col]) and pd.isnull(data[col]).any():
                data[col].fillna(data[col].mean(), inplace=True)
            else:
                if pd.isnull(data[col]).any():
                    data[col].fillna(data[col].mode()[0], inplace=True)

        return data

    @task
    def statistical_analysis(data):
        #Calculate the statistics of age and gender column 
        age_median = data['age'].median()
        age_std = data['age'].std()
        gender_mode = data['gender'].mode()[0]

        return data
    @task
    def save_to_csv(data):
       
        dag_directory = os.path.dirname(os.path.abspath(__file__))   #path where file will be saved
        csv_file_path = os.path.join(dag_directory, 'transformed_data.csv')
        data.to_csv(csv_file_path, index=False)

    data = data_ingestion()
    cleaned_data = data_cleaning(data)
    transformed_data = transformation(cleaned_data)
    statistical_analysis(transformed_data)
    
    save_to_csv(transformed_data)

my_dag_instance = red_dag()

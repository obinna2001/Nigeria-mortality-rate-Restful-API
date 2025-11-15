from dotenv import load_dotenv
from typing import Any, List, Tuple, Union
from src.services.database_service import retrieve_file_path
import os
import json
import pandas as pd

# load .env file
load_dotenv()

def retrieve_file_path(task_id: str) -> Tuple[bool, str, List[Any]]:
    """This function retrieves data from the health api database base on the task id
        args:
            task_id: A unique id created during every upload_file http request
        return: 
            - (bool, str, List[Any])
    """
    # get health-api database path
    json_path = os.getenv("DB_PATH")
    
    # validate if path exist
    if not json_path or not os.path.exists(json_path):
        return False, "data base not found", []
    
    # load database using async method
    with open(json_path, 'r') as file:
        content = file.read()
        db_data = json.loads(content)
    
    # check if input task_id id valid
    if task_id not in db_data:
        return False, "invalid task id", []
        
    # retrieve info from database base on task_id 
    query_data = db_data[task_id]['uploadfile']
    
    # return result if successful
    return True, 'Successful', [query_data]


def CleanUploadFile(job_id : str) -> Union[Tuple[bool, Tuple[pd.DataFrame, pd.DataFrame]], Tuple[bool, str]]:
    """Retrieve and Clean uploaded file
        args:
            job_id: A unique identify to extract user uploaded file
        returns:
            - (bool, dataframe)
                dfs: A Tuple of dataframe contain the cleaned and uncleaned df
                bool: True
            - (bool, message)
               bool: False
               message: An error message
    """
    # retrieve file path based on Job id
    status, message, output = retrieve_file_path(job_id)   
    if not status: # check if status is False i.e job id or db does not exist 
        return status, message   
    
    file_path = " ".join(output)
    df = pd.read_csv(file_path) # convert csv file to a dataframe      
    if 'index' in df.columns.to_list():  # drop index column if it exist
        df = df.drop(columns=['index'])
    
    # create a new dataframe based us based on the neccessary columns
    df = (
        df[
            [
                'GHO (CODE)', 'YEAR (DISPLAY)', 'REGION (DISPLAY)', 'AGEGROUP (DISPLAY)', 'SEX (DISPLAY)',
                'COUNTRY (DISPLAY)', 'SEX (CODE)', 'GHECAUSES (DISPLAY)', 'CHILDCAUSE (DISPLAY)', 'Numeric'
            ]
        ]
    )
    
    df = df[(df['GHO (CODE)'] != "#indicator+code") & (df['GHO (CODE)'] != "GBD_DALYRTAGE")]  # remove invalid rows
    uncleaned_df = df.copy()  # create an uncleaned dataframe before cleaning
    
    # fill missing values in GHECAUSES (DISPLAY) with CHILDCAUSE (DISPLAY)
    df.loc[df['GHECAUSES (DISPLAY)'].isna(), 'GHECAUSES (DISPLAY)'] = df['CHILDCAUSE (DISPLAY)']
    df = df.dropna(subset=['GHECAUSES (DISPLAY)']) # drop all rows where GHECAUSES (DISPLAY) is null
    df['Numeric'] = df['Numeric'].astype(float).round(2)  # convert to float
    df['YEAR (DISPLAY)'] = pd.to_datetime(df['YEAR (DISPLAY)']).dt.year
    df = df.bfill().ffill()   # fill all nan values
    df = df.drop_duplicates()    # drop duplicates
 
    # return a clean and uncleaned df 
    return True, (df, uncleaned_df)
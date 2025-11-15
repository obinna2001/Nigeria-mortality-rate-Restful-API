import pandas as pd
from typing import List, Dict

def TotalColumnsAndRows(dataframe: pd.DataFrame) -> List[Dict]:
    """This function extracts and returns the total number of columns and rows in a dataframe
        args:
            dataframe: a pandas dataframe
        return:
            result: a list of dictionary contain the total number of rows and columns
    """
    # instantiate a dataframe
    df = dataframe.copy()
    
    # extracting the number of rows and columns
    result = [
        {
            'NumberOfRows': df.shape[0],
            'NumberOfColumns': df.shape[1]
        }
    ]
    
    return result

def PercentageMissingValues(dataframe : pd.DataFrame) -> List[Dict]:
    """Extract the percentage of missing values from a dataframe
        args:
            dataframe: a pandas dataframe
        returns:
            result: a list of dictionary containing the percentage of missing value per column
    """
    # Instantiate a dataframe
    df = dataframe.copy()
    # percentage of missing value
    missing_value = (df.isna().sum()/df.shape[0] * 100).round(2)
    
    result = (
        missing_value
        .to_frame()
        .reset_index()
        .rename(columns={'index':'column', 0:"missing value %"})   
        .to_dict(orient="records")
    ) # creates a list of dictionaries 
    
    # return result
    return [result]

def CategoricalSummary(dataframe: pd.DataFrame) -> List[Dict]:
    """Extract the summary of the categorical columns in a  dataframe
        args:
            dataframe: a pandas dataframe
        returns:
            result: a list of dictionary containing the categorical summaries
    """
    df = dataframe.copy()
    cat_summary = df.describe(include=[object])
    result = cat_summary.to_dict()
    return [result]

def NumericalSummary(dataframe: pd.DataFrame) -> List[Dict]:
    """Extract the summary of the numerical columns in a  dataframe
        args:
            dataframe: a pandas dataframe
        returns:
            result: a list of dictionary containing the numerical summary
    """
    df = dataframe.copy()
    num_summary = df.describe(exclude=[object])
    result = num_summary.to_dict()
    return [result]   
    
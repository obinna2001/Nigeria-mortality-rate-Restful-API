import pandas as pd
from typing import List, Dict
    
def FileSchema(dataframe: pd.DataFrame) -> List[Dict]:
    """Extract the schema info from a dataframe
        args:
            dataframe: a pandas dataframe
        returns:
            result: a list of dictionary containing the schema of a dataframe
    """
    df = dataframe.copy()
    schema_list = []
    for col in df.columns:
        schema_list.append({
            "column": col,
            "dtype": str(df[col].dtype),
            "count": df[col].notnull().sum()
        })

    return schema_list

def FileSample(dataframe: pd.DataFrame) -> List[Dict]:
    """Extract the first 5 rows of a dataframe
        args:
            dataframe: a pandas dataframe
        returns:
            result: a list of dictionary containing the first 5 rowsof a dataframe
    """
    df = dataframe.copy()
    df_sample = df.head(5).to_dict()

    return [df_sample]

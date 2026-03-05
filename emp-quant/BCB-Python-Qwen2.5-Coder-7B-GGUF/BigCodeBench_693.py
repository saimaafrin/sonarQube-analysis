
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(tuples_list, columns):
    """
    Convert a list of tuples into a Pandas DataFrame, perform a default scaling in each column, and return the transformed DataFrame.
    
    Parameters:
    tuples_list (list of tuples): The list of tuples to be converted into a DataFrame.
    columns (list of str): The column names for the DataFrame.
    
    Returns:
    df_scaled (DataFrame): A pandas DataFrame containing the scaled versions of the original data.
    """
    # Convert the list of tuples into a DataFrame
    df = pd.DataFrame(tuples_list, columns=columns)
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the DataFrame
    df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=columns)
    
    return df_scaled
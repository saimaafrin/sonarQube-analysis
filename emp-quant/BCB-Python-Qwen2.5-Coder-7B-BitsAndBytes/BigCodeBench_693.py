
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(tuples_list, columns):
    """
    Convert a list of tuples into a Pandas DataFrame, perform a default scaling in each column,
    and return the transformed DataFrame.

    Parameters:
    - tuples_list: List of tuples representing the data.
    - columns: List of strings representing the column names.

    Returns:
    - df_scaled (DataFrame): A pandas DataFrame containing the scaled versions of the original data.
    """
    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(tuples_list, columns=columns)
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the DataFrame
    df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=columns)
    
    return df_scaled
import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(data):
    """
    Scales numeric columns of a data dictionary using the StandardScaler.
    
    Parameters:
    - data: pd.DataFrame
    
    Returns:
    - pd.DataFrame: Dataframe with scaled numeric columns.
    """
    scaler = StandardScaler()
    numeric_cols = data.select_dtypes(include=[float, int]).columns
    data[numeric_cols] = data[numeric_cols].apply(lambda x: pd.to_numeric(x, errors='coerce'))
    scaled_data = pd.DataFrame(scaler.fit_transform(data[numeric_cols]), columns=numeric_cols)
    data.update(scaled_data)
    return data
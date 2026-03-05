
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(tuples_list, columns):
    # Convert the list of tuples into a DataFrame
    df = pd.DataFrame(tuples_list, columns=columns)
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the DataFrame
    df_scaled = scaler.fit_transform(df)
    
    # Convert the scaled data back to a DataFrame
    df_scaled = pd.DataFrame(df_scaled, columns=columns)
    
    return df_scaled
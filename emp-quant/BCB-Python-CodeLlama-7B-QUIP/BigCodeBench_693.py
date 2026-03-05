
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(tuples_list, columns):
    # Create a Pandas DataFrame from the list of tuples
    df = pd.DataFrame(tuples_list, columns=columns)

    # Create a StandardScaler object
    scaler = StandardScaler()

    # Scale the DataFrame using the StandardScaler
    df_scaled = scaler.fit(df)

    return df_scaled
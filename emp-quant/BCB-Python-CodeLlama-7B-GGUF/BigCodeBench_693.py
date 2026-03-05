
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(tuples_list, columns):
    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(tuples_list, columns=columns)

    # Create a StandardScaler object
    scaler = StandardScaler()

    # Scale each column of the DataFrame
    df_scaled = scaler.fit_transform(df)

    return df_scaled
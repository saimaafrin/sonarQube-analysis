
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(tuples_list, columns):
    # Create a DataFrame from the tuples list
    df = pd.DataFrame(tuples_list, columns=columns)

    # Create a StandardScaler object
    scaler = StandardScaler()

    # Scale each column of the DataFrame
    for col in df.columns:
        df[col] = scaler.fit_transform(df[col].values.reshape(-1, 1))

    return df

df_scaled = task_func(tuples_list, columns)

print(df_scaled)
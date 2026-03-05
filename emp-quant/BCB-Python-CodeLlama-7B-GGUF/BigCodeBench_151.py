
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(data_dict, data_keys):
    # Check if any of the keys in data_keys are not present in data_dict
    if not set(data_keys).issubset(data_dict.keys()):
        raise ValueError("No keys in data_keys are found in data_dict")

    # Create a DataFrame from the data_dict
    df = pd.DataFrame(data_dict)

    # Select the columns corresponding to the data_keys
    df_normalized = df[data_keys]

    # Scale the data using MinMaxScaler
    scaler = MinMaxScaler()
    df_normalized_scaled = scaler.fit_transform(df_normalized)

    # Create a new DataFrame with the scaled data
    df_normalized_scaled = pd.DataFrame(df_normalized_scaled, columns=df_normalized.columns)

    # Plot the scaled data
    fig, ax = plt.subplots()
    df_normalized_scaled.plot(ax=ax)

    return df_normalized_scaled, ax
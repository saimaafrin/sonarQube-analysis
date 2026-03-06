
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(data):
    # Normalize the data using MinMaxScaler
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data)
    
    # Convert the normalized data back to a DataFrame
    df_normalized = pd.DataFrame(normalized_data, columns=data.columns)
    
    # Calculate the average of each row
    df_normalized['Average'] = df_normalized.mean(axis=1)
    
    # Plotting the averages
    fig, ax = plt.subplots()
    ax.bar(range(len(df_normalized)), df_normalized['Average'], color='blue')
    ax.set_xlabel('Row Index')
    ax.set_ylabel('Average Value')
    ax.set_title('Averages of Rows in Normalized Dataset')
    
    return df_normalized, ax
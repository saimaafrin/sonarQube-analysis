
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(data):
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data
    normalized_data = scaler.fit_transform(data)
    
    # Convert the normalized data back to a DataFrame
    normalized_df = pd.DataFrame(normalized_data, columns=data.columns)
    
    # Calculate the average of each row
    normalized_df['Average'] = normalized_df.mean(axis=1)
    
    # Plot the average values
    plt.figure(figsize=(10, 6))
    plt.bar(range(1, len(normalized_df) + 1), normalized_df['Average'], color='blue')
    plt.xlabel('Row Index')
    plt.ylabel('Average Value')
    plt.title('Average Value of Each Row')
    plt.show()
    
    return normalized_df, plt.gca()
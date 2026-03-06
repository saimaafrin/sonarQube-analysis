
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(data):
    scaler = StandardScaler()
    scaled_data = {}
    
    for column in data.columns:
        try:
            # Attempt to convert the column to float
            data[column] = data[column].astype(float)
            # Scale the column if successful
            scaled_data[column] = scaler.fit_transform(data[[column]])
        except ValueError:
            # Leave the column unchanged if conversion fails
            scaled_data[column] = data[column]
    
    return pd.DataFrame(scaled_data)
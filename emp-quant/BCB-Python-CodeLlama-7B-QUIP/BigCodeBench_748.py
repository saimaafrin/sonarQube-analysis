
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(df, age, weight):
    # Filter the DataFrame based on the specified age and weight criteria
    filtered_df = df[df['Age'] < age and df['Weight'] > weight]

    # Check if the filtered DataFrame is empty
    if filtered_df.empty:
        raise KeyError("The input DataFrame does not contain the required columns 'Age' and 'Weight'")

    # Standardize the numerical values in the filtered DataFrame
    scaler = StandardScaler()
    scaled_df = pd.DataFrame(scaler.fit_transform(filtered_df), columns=filtered_df.columns)

    return scaled_df
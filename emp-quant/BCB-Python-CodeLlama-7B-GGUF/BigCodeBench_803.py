
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(file_name: str) -> pd.DataFrame:
    df = pd.read_csv(file_name)
    numeric_columns = df.select_dtypes(include=[np.number])
    if not numeric_columns.empty:
        scaler = MinMaxScaler()
        scaled_data = scaler.fit_transform(numeric_columns)
        scaled_df = pd.DataFrame(scaled_data, columns=numeric_columns.columns)
        return scaled_df
    else:
        raise ValueError("Input does not have numeric columns.")
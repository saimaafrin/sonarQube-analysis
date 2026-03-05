
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(file_name: str) -> pd.DataFrame:
    df = pd.read_csv(file_name)
    numeric_columns = df.select_dtypes(include=['number'])
    numeric_columns = MinMaxScaler().fit_transform(numeric_columns)
    return pd.DataFrame(numeric_columns, columns=numeric_columns.columns)
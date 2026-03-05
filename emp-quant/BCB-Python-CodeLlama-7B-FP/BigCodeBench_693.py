import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(tuples_list, columns):
    """
    Convert a list of tuples into a Pandas DataFrame, perform a default scaling in each column, and return the transformed DataFrame.
    """
    # Create a Pandas DataFrame from the list of tuples
    df = pd.DataFrame(tuples_list, columns=columns)

    # Create a StandardScaler object
    scaler = StandardScaler()

    # Scale each column of the DataFrame using the StandardScaler
    df_scaled = scaler.fit_transform(df)

    return df_scaled
tuples_list = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
]
columns = ["a", "b", "c"]
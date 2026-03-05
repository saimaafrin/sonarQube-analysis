import pandas as pd
from sklearn.linear_model import LinearRegression
def task_func(d, target='z'):
    """
    Perform linear regression to "x," "y," against "z" from a list of dictionaries "d."
    """
    # Convert the list of dictionaries to a Pandas DataFrame
    df = pd.DataFrame(d)

    # Drop any rows with missing values
    df.dropna(inplace=True)

    # Create a new column for the target variable
    df[target] = df[target].astype(float)

    # Perform linear regression
    model = LinearRegression().fit(df[['x', 'y']], df[target])

    return model
data = [{'x': 4, 'y': 20, 'z': 10}, {'x': 5, 'y': 25, 'z': 15}, {'x': 6, 'y': 5, 'z': 20}]
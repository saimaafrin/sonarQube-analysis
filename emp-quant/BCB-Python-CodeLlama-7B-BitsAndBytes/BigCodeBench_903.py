
import pandas as pd
from sklearn.linear_model import LinearRegression

def task_func(d, target='z'):
    # Convert the list of dictionaries to a Pandas DataFrame
    df = pd.DataFrame(d)

    # Perform linear regression on the "x" and "y" columns against the "z" column
    model = LinearRegression().fit(df[['x', 'y']], df[target])

    # Return the LinearRegression model
    return model
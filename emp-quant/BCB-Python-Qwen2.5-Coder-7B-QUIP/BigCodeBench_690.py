
import pandas as pd
from sklearn.linear_model import LinearRegression
ROWS = 100
COLUMNS = ['X', 'Y']

def task_func(df):
    # Generate random data for X and Y
    df = pd.DataFrame({
        'X': range(ROWS),
        'Y': range(ROWS)
    })

    # Initialize the linear regression model
    model = LinearRegression()

    # Fit the model to the data
    model.fit(df[['X']], df['Y'])

    return model
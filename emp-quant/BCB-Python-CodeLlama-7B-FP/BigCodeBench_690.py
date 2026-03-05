import pandas as pd
from sklearn.linear_model import LinearRegression
ROWS = 100
COLUMNS = ['X', 'Y']
def task_func(df):
    # Create a random dataset
    df = pd.DataFrame(np.random.rand(ROWS, COLUMNS), columns=COLUMNS)

    # Fit a linear regression model to the data
    model = LinearRegression().fit(df[['X']], df['Y'])

    # Print the model
    print(model)

    # Return the model
    return model
df = pd.DataFrame(np.random.rand(ROWS, COLUMNS), columns=COLUMNS)
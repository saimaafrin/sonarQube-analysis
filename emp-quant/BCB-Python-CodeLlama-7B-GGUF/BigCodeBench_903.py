
import pandas as pd
from sklearn.linear_model import LinearRegression

def task_func(d, target='z'):
    # Convert list of dictionaries to a Pandas DataFrame
    df = pd.DataFrame(d)

    # Perform linear regression on the target variable
    model = LinearRegression().fit(df[target], df['z'])

    return model

print(model)
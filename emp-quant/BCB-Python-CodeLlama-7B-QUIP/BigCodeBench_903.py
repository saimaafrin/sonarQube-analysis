
import pandas as pd
from sklearn.linear_model import LinearRegression

def task_func(d, target='z'):
    data = pd.DataFrame(d)
    model = LinearRegression(data[target])
    return model

data = [{'x': 4, 'y': 20, 'z': 10}, {'x': 5, 'y': 25, 'z': 15}, {'x': 6, 'y': 5, 'z': 20}]
model = task_func(data, target='y')
print(model)
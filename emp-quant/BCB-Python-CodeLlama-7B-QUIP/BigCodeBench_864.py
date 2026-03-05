
import pandas as pd
import numpy as np

def task_func(fruit_data):
    if len(fruit_data) == 0:
        return pd.DataFrame()
    fruit_data = pd.DataFrame(fruit_data, columns=['Fruit', 'Count'])
    fruit_data['Total Count'] = fruit_data['Fruit'].map(fruit_data['Fruit'].value_counts())
    fruit_data['Average Count'] = fruit_data['Fruit'].map(fruit_data['Fruit'].mean())
    fruit_data = fruit_data.sort_values(by='Fruit')
    return fruit_data
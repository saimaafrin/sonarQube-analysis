
import pandas as pd
import numpy as np

def task_func(days, random_seed=0):
    np.random.seed(random_seed)
    expenditure_data = np.random.randint(0, 100, size=(days, 5))
    expenditure_data.columns = ['Groceries', 'Entertainment', 'Rent', 'Utilities', 'Miscellaneous']
    expenditure_data.index = pd.date_range(start='2023-01-01', periods=days)
    return expenditure_data
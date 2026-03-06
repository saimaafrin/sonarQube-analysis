
import numpy as np
from scipy import stats

def task_func(df):
    results = {}
    for column in df.columns:
        _, p_value = stats.shapiro(df[column])
        results[column] = p_value
    return results

import numpy as np
from scipy import stats

def task_func(df):
    p_values = {}
    for column in df.columns:
        p_value = stats.shapiro(df[column])[1]
        p_values[column] = p_value
    return p_values
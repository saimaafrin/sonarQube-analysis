
import numpy as np
from scipy import stats
def task_func(df):
    p_values = {}
    for column in df.columns:
        _, p_value = stats.shapiro(df[column])
        p_values[column] = p_value
    return p_values
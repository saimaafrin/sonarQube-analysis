
import numpy as np
import pandas as pd
from scipy.stats import linregress

def task_func(df):
    # Perform linear regression on the two variables
    slope, intercept, r_value, p_value, std_err = linregress(df['var1'], df['var2'])

    # Add a 'predicted' column to the DataFrame
    df['predicted'] = intercept + slope * df['var1']

    return df
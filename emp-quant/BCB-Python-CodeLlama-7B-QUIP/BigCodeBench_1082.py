
import pandas as pd
from scipy.stats import pearsonr

def task_func(data):
    # Convert scores from string format to floats
    data['scores'] = data['scores'].astype(float)

    # Encode categorical grades into numerical values based on their rank order
    data['grades'] = data['grades'].rank()

    # Compute the Pearson correlation coefficient between the numerical scores and encoded grades
    correlation = pearsonr(data['scores'], data['grades'])

    return correlation
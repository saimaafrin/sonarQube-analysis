
import pandas as pd
from scipy.stats import pearsonr

def task_func(data):
    # Convert scores from string format to floats
    data['score'] = data['score'].astype(float)

    # Encode categorical grades into numerical values based on their rank order
    data['grade'] = data['grade'].rank(method='dense')

    # Compute the Pearson correlation coefficient between the numerical scores and the encoded grades
    correlation = pearsonr(data['score'], data['grade'])[0]

    return correlation

import pandas as pd
from scipy.stats import pearsonr

def task_func(data):
    # Check if the data frame has less than 2 rows
    if len(data) < 2:
        return float('NaN')
    
    # Convert scores from string format to floats
    data['score'] = data['score'].astype(float)
    
    # Encode categorical grades into numerical values based on their rank order
    grade_order = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'F': 5}
    data['grade'] = data['grade'].map(grade_order)
    
    # Compute the Pearson correlation coefficient
    correlation, _ = pearsonr(data['score'], data['grade'])
    
    return correlation
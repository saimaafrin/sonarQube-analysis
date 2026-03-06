
import pandas as pd
from scipy.stats import pearsonr

def task_func(data):
    # Check if the dataframe has at least 2 rows
    if len(data) < 2:
        return float('NaN')
    
    # Convert scores from string to float
    data['score'] = data['score'].astype(float)
    
    # Encode categorical grades into numerical values
    grade_mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
    data['grade_encoded'] = data['grade'].map(grade_mapping)
    
    # Calculate the Pearson correlation coefficient
    correlation, _ = pearsonr(data['score'], data['grade_encoded'])
    
    return correlation
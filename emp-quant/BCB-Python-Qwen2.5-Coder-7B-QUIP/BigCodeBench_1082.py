
import pandas as pd
from scipy.stats import pearsonr

def task_func(data):
    # Check if the DataFrame has less than 2 rows
    if len(data) < 2:
        return float('NaN')
    
    # Convert scores from string format to floats
    data['scores'] = pd.to_numeric(data['scores'], errors='coerce')
    
    # Encode categorical grades into numerical values based on their rank order
    grade_to_rank = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'F': 5}
    data['grades'] = data['grades'].map(grade_to_rank).astype(float)
    
    # Compute the Pearson correlation coefficient
    correlation, _ = pearsonr(data['scores'], data['grades'])
    
    return correlation
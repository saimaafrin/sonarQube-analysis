import pandas as pd
from scipy.stats import pearsonr
import numpy as np
def task_func(data):
    """
    Calculates the Pearson correlation coefficient between numerical scores and categorical grades.
    
    Parameters:
    data (pd.DataFrame): A pandas DataFrame with two columns: 'score' (string) and 'grade' (categorical).
    
    Returns:
    correlation (float): The Pearson correlation coefficient between the converted numerical scores and encoded grades.
    Returns NaN if the input data frame has less than 2 rows.
    """
    if len(data) < 2:
        return np.nan
    
    # Convert scores from string to float
    data['score'] = data['score'].astype(float)
    
    # Encode categorical grades into numerical values based on their rank order
    grade_order = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'F': 5}
    data['grade'] = data['grade'].map(grade_order)
    
    # Calculate the Pearson correlation coefficient
    correlation, _ = pearsonr(data['score'], data['grade'])
    
    return correlation
data = pd.DataFrame({
    'score': ['85', '92', '78', '90', '88'],
    'grade': ['B', 'A', 'C', 'A', 'B']
})
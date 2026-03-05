import pandas as pd
from scipy.stats import pearsonr
def task_func(data):
    """
    Calculates the Pearson correlation coefficient between numerical scores and categorical grades.
    This function performs three main tasks:
        1. Converts scores from string format to floats.
        2. Encodes categorical grades into numerical values based on their rank order.
        3. Computes the Pearson correlation coefficient between the numerical scores and the encoded grades.
    The function should output with:
        correlation (float): The Pearson correlation coefficient between the converted numerical scores and encoded grades.
        Returns NaN if the input data frame has less than 2 rows, as the correlation coefficient cannot be calculated in this case.
    """
    # Check if the input data frame has less than 2 rows
    if len(data) < 2:
        return float('NaN')

    # Convert scores from string format to floats
    data['scores'] = data['scores'].astype(float)

    # Encode categorical grades into numerical values based on their rank order
    data['grades'] = data['grades'].rank(method='dense')

    # Compute the Pearson correlation coefficient between the numerical scores and the encoded grades
    correlation = pearsonr(data['scores'], data['grades'])[0]

    return correlation
data = pd.DataFrame({'scores': ['10', '20', '30', '40', '50'],
                     'grades': ['A', 'B', 'C', 'D', 'F']})
import pandas as pd
from scipy.stats import pearsonr
def task_func(data):
    """
    Calculates the Pearson correlation coefficient between numerical scores and categorical grades.

    Parameters
    ----------
    data : pandas.DataFrame
        A data frame with numerical scores and categorical grades.

    Returns
    -------
    correlation : float
        The Pearson correlation coefficient between the converted numerical scores and encoded grades.
    """
    # Convert scores from string format to floats
    data['scores'] = data['scores'].astype(float)

    # Encode categorical grades into numerical values based on their rank order
    data['grades'] = data['grades'].rank(method='dense')

    # Compute the Pearson correlation coefficient between the numerical scores and encoded grades
    correlation = pearsonr(data['scores'], data['grades'])[0]

    # Return the correlation coefficient
    return correlation
data = pd.DataFrame({'scores': [80, 70, 90, 85, 75], 'grades': ['A', 'B', 'A', 'B', 'C']})
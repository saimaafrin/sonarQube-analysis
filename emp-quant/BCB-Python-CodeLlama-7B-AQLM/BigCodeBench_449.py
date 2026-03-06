import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
def task_func(data: pd.DataFrame) -> (pd.DataFrame, list):
    """
    This function takes a pandas DataFrame and standardizes its features using sklearn's StandardScaler,
    which standardizes features by removing the mean and scaling to unit variance.
    After standardization, it draws a histogram for each feature with 20 bins.

    Parameters:
    - data (pd.DataFrame): The input data to be standardized and plotted. It is expected to have
                           columns named 'Feature1', 'Feature2', 'Feature3', 'Feature4', and 'Feature5'.
                           If there are additional data columns, they are ignored.


    Returns:
    - standardized_data (pd.DataFrame): The standardized data.
    - axes_list (list): A list of matplotlib Axes objects representing the histograms for each feature.

    Requirements:
    - pandas
    - matplotlib.pyplot
    - sklearn.preprocessing.StandardScaler
    
    Example:
    >>> data = pd.DataFrame({
    ...     'Feature1': [0.5, 0.6, 0.7, 0.8, 0.9],
    ...     'Feature2': [0.1, 0.2, 0.3, 0.4, 0.5],
    ...     'Feature3': [0.9, 0.8, 0.7, 0.6, 0.5],
    ...     'Feature4': [0.5, 0.4, 0.3, 0.2, 0.1],
    ...     'Feature5': [0.1, 0.3, 0.5, 0.7, 0.9]
    ... })
    >>> standardized_data, axes_list = task_func(data)
    >>> type(standardized_data)
    <class 'pandas.core.frame.DataFrame'>
    >>> axes_list
    [<Axes: title={'center': 'Histogram of Feature1'}>, <Axes: title={'center': 'Histogram of Feature2'}>, <Axes: title={'center': 'Histogram of Feature3'}>, <Axes: title={'center': 'Histogram of Feature4'}>, <Axes: title={'center': 'Histogram of Feature5'}>]
    >>> type(axes_list[0])
    <class 'matplotlib.axes._axes.Axes'>
    """
    # TODO: Implement the task
    # Hint: You can use the following code to draw a histogram for a feature:
    #       plt.hist(data['Feature1'], bins=20)
    #       plt.title('Histogram of Feature1')
    #       plt.show()
    #       plt.close()
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
    #       plt.cla()
    #       plt.close('all')
    #       plt.clf()
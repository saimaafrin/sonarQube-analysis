from datetime import datetime
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
TEMP_CATEGORIES = ['Cold', 'Normal', 'Hot']
FILE_PATH = 'custom_data.csv'
def task_func(hours, file_path=FILE_PATH):
    """
    Generate temperature data for the specified number of hours, save it in a CSV file, 
    and plot the data using matplotlib.
    
    Parameters:
    hours (int): The number of hours for which temperature data is to be generated.
    file_path (str, optional): Path where the CSV file will be saved. Defaults to 'temp_data.csv'.
    
    Returns:
    tuple: 
        - str: The path of the generated CSV file.
        - Axes: The plot object for further manipulation or saving.
    
    Requirements:
    - pandas
    - datetime
    - random
    - matplotlib.pyplot
    
    Data Structure:
    The function uses a dictionary to manage the generated temperature data with keys: 'Time', 'Temperature', and 'Category'.
    
    Example:
    >>> file_path, ax = task_func(24)
    >>> isinstance(file_path, str)
    True
    >>> 'custom_data.csv' in file_path
    True
    """
    data = {}
    data['Time'] = []
    data['Temperature'] = []
    data['Category'] = []
    for i in range(hours):
        data['Time'].append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        data['Temperature'].append(randint(10, 40))
        data['Category'].append(TEMP_CATEGORIES[randint(0, 2)])
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    ax = df.plot(x='Time', y='Temperature', kind='line', title='Temperature Data')
    return file_path, ax
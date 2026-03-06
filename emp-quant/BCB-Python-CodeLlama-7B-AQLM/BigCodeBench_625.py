import math
from random import randint
import pandas as pd
def task_func(cities_list):
    """
    Generate a DataFrame with population data for a list of cities. The population is generated randomly 
    and rounded up to the next thousand.
    
    Requirements:
    - pandas
    - math
    - random

    Parameters:
    cities_list (list): A list of city names.
    
    Returns:
    DataFrame: A pandas DataFrame with columns 'City' and 'Population', containing population data for the cities.

    Example:
    >>> cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    >>> pop_data = task_func(cities)
    >>> type(pop_data)
    <class 'pandas.core.frame.DataFrame'>
    """
    # Create a list of tuples with city names and population data
    pop_data = [(city, randint(1000, 1000000)) for city in cities_list]
    # Create a DataFrame with the population data
    df = pd.DataFrame(pop_data, columns=['City', 'Population'])
    # Round the population data to the next thousand
    df['Population'] = df['Population'].apply(lambda x: math.ceil(x / 1000) * 1000)
    return df
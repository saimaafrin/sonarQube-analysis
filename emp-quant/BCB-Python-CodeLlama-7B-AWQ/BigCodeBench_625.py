import math
from random import randint
import pandas as pd
def task_func(cities_list):
    """
    Generate a DataFrame with population data for a list of cities.
    The population is generated randomly and rounded up to the next thousand.
    """
    population_data = []
    for city in cities_list:
        population = randint(1000, 10000)
        population_data.append({'City': city, 'Population': population})
    return pd.DataFrame(population_data)
cities_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
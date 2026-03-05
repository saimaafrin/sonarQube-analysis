import math
from random import randint
import pandas as pd
def task_func(cities_list):
    """
    Generate a DataFrame with population data for a list of cities.
    The population is generated randomly and rounded up to the next thousand.
    """
    population_list = []
    for city in cities_list:
        population = randint(1, 10000)
        population_list.append(round(population, -3))
    df = pd.DataFrame({'City': cities_list, 'Population': population_list})
    return df
cities_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
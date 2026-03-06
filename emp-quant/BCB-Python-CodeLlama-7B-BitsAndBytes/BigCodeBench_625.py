
import math
from random import randint
import pandas as pd

def task_func(cities_list):
    population_data = []
    for city in cities_list:
        population = randint(1000, 100000)
        population_data.append({'City': city, 'Population': population})
    return pd.DataFrame(population_data)

import math
from random import randint
import pandas as pd

def task_func(cities_list):
    population_data = []
    for city in cities_list:
        population = math.ceil(randint(1000, 100000) / 1000) * 1000
        population_data.append({'City': city, 'Population': population})
    
    df = pd.DataFrame(population_data)
    return df
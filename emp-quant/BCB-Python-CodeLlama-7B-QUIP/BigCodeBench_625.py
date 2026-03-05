
import math
from random import randint
import pandas as pd

def task_func(cities_list):
    population_list = []
    for city in cities_list:
        population = randint(0, 1000)
        population_list.append((city, population))
    population_df = pd.DataFrame(population_list, columns=['City', 'Population'])
    return population_df
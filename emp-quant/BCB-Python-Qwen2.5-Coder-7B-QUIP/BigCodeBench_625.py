
import math
from random import randint
import pandas as pd

def task_func(cities_list):
    # Generate population data for each city
    population_data = {}
    for city in cities_list:
        population = math.ceil(randint(10000, 500000))  # Random population between 10,000 and 500,000
        population_data[city] = population

    # Create a DataFrame from the population data
    df = pd.DataFrame(list(population_data.items()), columns=['City', 'Population'])

    return df
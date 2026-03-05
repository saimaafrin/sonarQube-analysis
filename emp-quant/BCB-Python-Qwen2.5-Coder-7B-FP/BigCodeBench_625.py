import math
from random import randint
import pandas as pd
def task_func(cities_list):
    # Initialize an empty list to store city and population data
    data = []
    
    # Loop through each city in the provided list
    for city in cities_list:
        # Generate a random population between 1000 and 1000000
        population = randint(1000, 1000000)
        # Round up the population to the nearest thousand
        population = math.ceil(population / 1000) * 1000
        # Append the city and its population to the data list
        data.append([city, population])
    
    # Create a pandas DataFrame from the data list
    df = pd.DataFrame(data, columns=['City', 'Population'])
    
    # Return the DataFrame
    return df
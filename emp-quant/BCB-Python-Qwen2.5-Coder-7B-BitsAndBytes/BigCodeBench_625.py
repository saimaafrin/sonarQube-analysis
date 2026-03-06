
import math
from random import randint
import pandas as pd

def task_func(cities_list):
    # Initialize an empty list to store city-population pairs
    city_population_data = []
    
    # Loop through each city in the provided list
    for city in cities_list:
        # Generate a random population between 100,000 and 5,000,000
        population = randint(100000, 5000000)
        
        # Round up the population to the nearest thousand
        rounded_population = math.ceil(population / 1000) * 1000
        
        # Append the city and its rounded population to the list
        city_population_data.append([city, rounded_population])
    
    # Create a DataFrame from the list of city-population pairs
    df = pd.DataFrame(city_population_data, columns=['City', 'Population'])
    
    return df
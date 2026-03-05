
import numpy as np
import matplotlib.pyplot as plt

# Constants
CITIES = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney', 'Paris', 'Berlin', 'Moscow', 'Madrid', 'Rome']

def task_func(city_dict, max_range=1000000, seed=0):
    # Seed the random number generator
    np.random.seed(seed)
    
    # Initialize the population dictionary
    population_dict = {city: -1 for city in CITIES}
    
    # Generate random populations for cities in the list
    for city in CITIES:
        if city in city_dict.values():
            population_dict[city] = np.random.randint(1, max_range + 1)
    
    # Extract city names and populations for plotting
    cities = list(population_dict.keys())
    populations = list(population_dict.values())
    
    # Create a bar chart of the city populations
    fig, ax = plt.subplots()
    ax.bar(cities, populations, color='blue')
    ax.set_xlabel('Cities')
    ax.set_ylabel('Population')
    ax.set_title('City Populations')
    
    return population_dict, ax
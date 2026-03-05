
import numpy as np
import matplotlib.pyplot as plt

# Constants
CITIES = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney', 'Paris', 'Berlin', 'Moscow', 'Madrid', 'Rome']

def task_func(city_dict, max_range=1000000, seed=0):
    # Seed the random number generator
    np.random.seed(seed)
    
    # Initialize the population dictionary
    population_dict = {city: -1 for city in CITIES}
    
    # Generate random populations for cities in city_dict
    for person, city in city_dict.items():
        if city in CITIES:
            population_dict[city] = np.random.randint(1, max_range)
    
    # Extract city names and populations for plotting
    cities = list(population_dict.keys())
    populations = list(population_dict.values())
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(cities, populations, color='skyblue')
    ax.set_xlabel('Cities')
    ax.set_ylabel('Population')
    ax.set_title('City Populations')
    
    # Show the plot
    plt.show()
    
    return population_dict, ax
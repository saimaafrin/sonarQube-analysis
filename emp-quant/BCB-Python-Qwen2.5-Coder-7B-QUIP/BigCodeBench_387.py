
import numpy as np
import matplotlib.pyplot as plt
# Constants
CITIES = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney', 'Paris', 'Berlin', 'Moscow', 'Madrid', 'Rome']

def task_func(city_dict, max_range=1000000, seed=0):
    # Seed the random number generator
    np.random.seed(seed)
    
    # Initialize a dictionary to store city populations
    city_populations = {}
    
    # Iterate over the city_dict and assign random populations
    for city, _ in city_dict.items():
        if city in CITIES:
            city_populations[city] = np.random.randint(1, max_range)
        else:
            city_populations[city] = -1
    
    # Plot the city populations
    fig, ax = plt.subplots()
    ax.bar(range(len(city_populations)), list(city_populations.values()), tick_label=list(city_populations.keys()))
    ax.set_xlabel('City')
    ax.set_ylabel('Population')
    ax.set_title('City Populations')
    
    return city_populations, ax
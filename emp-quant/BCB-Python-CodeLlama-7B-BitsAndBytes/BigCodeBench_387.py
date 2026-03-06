
import numpy as np
import matplotlib.pyplot as plt
# Constants
CITIES = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney', 'Paris', 'Berlin', 'Moscow', 'Madrid', 'Rome']
def task_func(city_dict, max_range=1000000, seed=0):
    # Generate random population values for each city
    np.random.seed(seed)
    city_populations = {}
    for city in CITIES:
        if city in city_dict:
            city_populations[city] = np.random.randint(1, max_range)
        else:
            city_populations[city] = -1
    # Plot the population data
    fig, ax = plt.subplots()
    ax.bar(CITIES, city_populations.values())
    ax.set_xticks(CITIES)
    ax.set_xticklabels(CITIES, rotation=90)
    ax.set_xlabel('City')
    ax.set_ylabel('Population')
    ax.set_title('City Populations')
    return city_populations, ax
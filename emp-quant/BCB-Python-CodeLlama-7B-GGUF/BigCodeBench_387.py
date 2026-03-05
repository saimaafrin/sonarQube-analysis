
import numpy as np
import matplotlib.pyplot as plt
# Constants
CITIES = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney', 'Paris', 'Berlin', 'Moscow', 'Madrid', 'Rome']
def task_func(city_dict, max_range=1000000, seed=0):
    # Generate random population values for each city
    np.random.seed(seed)
    city_populations = {city: np.random.randint(1, max_range) for city in CITIES}
    # Add -1 for cities not in the list
    for city in city_dict:
        if city not in CITIES:
            city_populations[city] = -1
    # Plot the data
    fig, ax = plt.subplots()
    ax.bar(CITIES, [city_populations[city] for city in CITIES])
    ax.set_title('City Populations')
    ax.set_xlabel('City')
    ax.set_ylabel('Population')
    return city_populations, ax

import numpy as np
import matplotlib.pyplot as plt
# Constants
CITIES = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney', 'Paris', 'Berlin', 'Moscow', 'Madrid', 'Rome']
def task_func(city_dict, max_range=1000000, seed=0):
    np.random.seed(seed)
    population_dict = {}
    for city in CITIES:
        if city in city_dict:
            population_dict[city] = np.random.randint(1, max_range)
        else:
            population_dict[city] = -1
    fig, ax = plt.subplots()
    ax.bar(CITIES, population_dict.values())
    ax.set_ylabel('Population')
    ax.set_xlabel('City')
    ax.set_title('City Population')
    return population_dict, ax
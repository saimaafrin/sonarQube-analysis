import numpy as np
import matplotlib.pyplot as plt
CITIES = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney', 'Paris', 'Berlin', 'Moscow', 'Madrid', 'Rome']
def task_func(city_dict, max_range=1000000, seed=0):
    """
    Generates a dictionary of city populations for the cities in the list and plots the population data using a bar chart.
    The population values are randomly generated integers between 1 and 'max_range' if the city is in the list of cities,
    otherwise the population value is -1. The random number generator is seeded with the value 'seed' before generating the population values.
    """
    # Generate population values for each city
    city_populations = {}
    for city in CITIES:
        if city in city_dict:
            city_populations[city] = np.random.randint(1, max_range, size=1)
        else:
            city_populations[city] = -1

    # Plot the population data
    fig, ax = plt.subplots()
    ax.bar(CITIES, city_populations.values())
    ax.set_ylabel('Population')
    ax.set_title('City Populations')
    plt.show()

    return city_populations, ax
city_dict = {'Alice': 'New York', 'Bob': 'London', 'Charlie': 'Beijing', 'David': 'Tokyo', 'Eve': 'Sydney', 'Frank': 'Paris', 'Grace': 'Berlin', 'Henry': 'Moscow', 'Iris': 'Madrid', 'Jack': 'Rome'}
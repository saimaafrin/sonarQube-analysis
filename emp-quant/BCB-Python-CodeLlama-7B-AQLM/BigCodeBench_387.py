import numpy as np
import matplotlib.pyplot as plt
CITIES = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney', 'Paris', 'Berlin', 'Moscow', 'Madrid', 'Rome']
def task_func(city_dict, max_range=1000000, seed=0):
    """
    Given a constant list of cities (CITIES) and a dictionary 'city_dict' of people's names and their favorite cities, 
    this function generates a dictionary of city populations for the cities in the list and plots the population 
    data using a bar chart. The population values are randomly generated integers between 1 and 'max_range' if 
    the city is in the list of cities, otherwise the population value is -1. The random number generator is seeded
    with the value 'seed' before generating the population values.

    Parameters:
    city_dict (dict): The dictionary with keys as people's names and values as city names. 
    max_range (int, Optional): The maximum population value for the randomly generated population. Defaults to 1000000.
    Must be greater than 1.
    seed (int, Optional): The seed for the random number generator. Defaults to 0.

    Returns:
    dict: A dictionary with city names as keys and randomly generated populations as values.
    matplotlib.axes.Axes: The Axes object of the plot for further manipulation or testing.

    Requirements:
    - numpy for random number generation
    - matplotlib for plotting

    Example:
    >>> city_dict = {'John': 'New York', 'Alice': 'London', 'Bob': 'Beijing', 'Charlie': 'Tokyo', 'David': 'Sydney'}
    >>> population_dict, plot_axes = task_func(city_dict)
    """
    # Check if max_range is greater than 1
    if max_range <= 1:
        raise ValueError('max_range must be greater than 1')

    # Generate random population values
    np.random.seed(seed)
    population_dict = {}
    for city in CITIES:
        if city in city_dict.values():
            population_dict[city] = np.random.randint(1, max_range)
        else:
            population_dict[city] = -1

    # Plot the population data
    fig, ax = plt.subplots()
    ax.bar(CITIES, population_dict.values())
    ax.set_title('Population of Cities')
    ax.set_xlabel('City')
    ax.set_ylabel('Population')
    ax.set_xticks(np.arange(len(CITIES)))
    ax.set_xticklabels(CITIES)
    ax.set_ylim(0, max_range)
    ax.set_yticks(np.arange(0, max_range, max_range/10))
    ax.set_yticklabels(np.arange(0, max_range, max_range/10))
    return population_dict, ax
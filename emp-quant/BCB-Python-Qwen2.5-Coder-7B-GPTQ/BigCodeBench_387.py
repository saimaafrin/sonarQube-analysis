import numpy as np
import matplotlib.pyplot as plt
CITIES = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney', 'Paris', 'Berlin', 'Moscow', 'Madrid', 'Rome']
def task_func(city_dict, max_range=1000000, seed=0):
    """
    Generates a dictionary of city populations for the cities in the list and plots the population data using a bar chart.
    
    Parameters:
    - city_dict: A dictionary of people's names and their favorite cities.
    - max_range: The maximum range for the randomly generated population values.
    - seed: The seed for the random number generator.
    
    Returns:
    - dict: A dictionary with city names as keys and randomly generated populations as values.
    - matplotlib.axes.Axes: The Axes object of the plot for further manipulation or testing.
    """
    # Seed the random number generator
    np.random.seed(seed)
    
    # Initialize the population dictionary
    population_dict = {city: -1 for city in CITIES}
    
    # Generate random populations for cities in the list
    for city in CITIES:
        if city in city_dict.values():
            population_dict[city] = np.random.randint(1, max_range)
    
    # Extract city names and populations for plotting
    cities = list(population_dict.keys())
    populations = list(population_dict.values())
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(cities, populations, color='blue')
    ax.set_xlabel('Cities')
    ax.set_ylabel('Population')
    ax.set_title('City Populations')
    
    return population_dict, ax
city_dict = {'Alice': 'New York', 'Bob': 'London', 'Charlie': 'Beijing'}
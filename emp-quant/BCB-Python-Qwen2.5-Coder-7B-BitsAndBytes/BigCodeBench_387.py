
import numpy as np
import matplotlib.pyplot as plt

# Constants
CITIES = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney', 'Paris', 'Berlin', 'Moscow', 'Madrid', 'Rome']

def task_func(city_dict, max_range=1000000, seed=0):
    # Seed the random number generator
    np.random.seed(seed)
    
    # Initialize an empty dictionary to store city populations
    city_populations = {}
    
    # Iterate over each city in the CITIES list
    for city in CITIES:
        # Check if the city is in the city_dict
        if city in city_dict.values():
            # Generate a random population within the specified range
            population = np.random.randint(1, max_range + 1)
        else:
            # Set population to -1 if the city is not in the city_dict
            population = -1
        
        # Add the city and its population to the dictionary
        city_populations[city] = population
    
    # Extract city names and populations for plotting
    cities = list(city_populations.keys())
    populations = list(city_populations.values())
    
    # Create a bar chart of city populations
    fig, ax = plt.subplots()
    ax.bar(cities, populations, color='blue')
    
    # Set labels and title
    ax.set_xlabel('Cities')
    ax.set_ylabel('Population')
    ax.set_title('City Populations')
    
    # Show the plot
    plt.show()
    
    # Return the dictionary of city populations and the Axes object
    return city_populations, ax
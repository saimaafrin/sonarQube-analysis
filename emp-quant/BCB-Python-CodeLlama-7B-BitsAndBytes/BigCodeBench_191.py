
import random
from scipy import stats

def task_func(animals, mean):
    # Initialize a dictionary to store the sales
    sales = {}

    # Simulate the sales
    for i in range(int(stats.poisson.rvs(mean))):
        # Choose a random animal from the list
        animal = random.choice(animals)

        # Increment the sales count for the chosen animal
        if animal in sales:
            sales[animal] += 1
        else:
            sales[animal] = 1

    # Return the sales summary
    return sales
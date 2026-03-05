
import random
from scipy import stats

def task_func(animals, mean):
    # Generate a Poisson distribution with the specified mean
    num_customers = stats.poisson.rvs(mean)

    # Initialize a dictionary to store the sales
    sales = {}

    # Simulate the sales for each customer
    for i in range(num_customers):
        # Randomly select an animal from the list
        animal = random.choice(animals)

        # Increment the number of sales for the selected animal
        if animal in sales:
            sales[animal] += 1
        else:
            sales[animal] = 1

    return sales
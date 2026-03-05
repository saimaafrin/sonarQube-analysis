import random
from scipy import stats
def task_func(animals, mean):
    """
    Simulates sales in a pet shop based on a randomly determined number of customers. Each customer randomly buys one type of animal from the specified list of animals. The function displays and returns a summary of the sales, where the number of customers follows a Poisson distribution with the specified mean (mu).
    """
    # Generate a random number of customers
    num_customers = int(stats.poisson.rvs(mu=mean))

    # Initialize a dictionary to store the sales
    sales = {}

    # Simulate the sales for each animal type
    for animal in animals:
        # Generate a random number of sales for the current animal type
        num_sales = int(stats.poisson.rvs(mu=num_customers * 0.2))

        # Add the sales to the dictionary
        sales[animal] = num_sales

    # Return the sales dictionary
    return sales
animals = ['dog', 'cat', 'fish']
mean = 10
import random
from scipy import stats
def task_func(animals, mean):
    """
    Simulates sales in a pet shop based on a randomly determined number of customers.
    Each customer randomly buys one type of animal from the specified list of animals.
    The function displays and returns a summary of the sales, where the number of customers follows a Poisson distribution with the specified mean (mu).
    """
    # Generate a random number of customers
    num_customers = stats.poisson.rvs(mean)

    # Create a dictionary to store the sales
    sales = {}

    # Simulate the sales for each customer
    for i in range(num_customers):
        # Generate a random animal type
        animal = random.choice(animals)

        # Increment the sale count for the animal
        if animal in sales:
            sales[animal] += 1
        else:
            sales[animal] = 1

    # Return the sales summary
    return sales
animals = ['dog', 'cat', 'fish', 'bird']
mean = 5
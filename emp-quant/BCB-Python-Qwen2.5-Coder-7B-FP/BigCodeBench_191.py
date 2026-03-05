import random
from scipy import stats
def task_func(animals, mean):
    # Generate a random number of customers following a Poisson distribution
    num_customers = stats.poisson.rvs(mu=mean)
    
    # Initialize a dictionary to store the number of sales for each animal type
    sales_summary = {animal: 0 for animal in animals}
    
    # Simulate each customer's purchase
    for _ in range(num_customers):
        # Randomly choose an animal type for the customer
        chosen_animal = random.choice(animals)
        # Increment the sales count for the chosen animal
        sales_summary[chosen_animal] += 1
    
    # Print the sales summary
    print(sales_summary)
    
    # Return the sales summary as a dictionary
    return sales_summary
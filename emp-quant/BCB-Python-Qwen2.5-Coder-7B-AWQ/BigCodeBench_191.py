import random
from scipy import stats
def task_func(animals, mean):
    # Initialize a dictionary to store the sales count for each animal
    sales_summary = {animal: 0 for animal in animals}
    
    # Generate a random number of customers based on the Poisson distribution
    num_customers = stats.poisson.rvs(mu=mean)
    
    # Simulate each customer's purchase
    for _ in range(num_customers):
        # Randomly select an animal type for the customer
        selected_animal = random.choice(animals)
        # Increment the sales count for the selected animal
        sales_summary[selected_animal] += 1
    
    # Print the sales summary
    print(sales_summary)
    
    # Return the sales summary as a dictionary
    return sales_summary
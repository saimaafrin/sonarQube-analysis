
import random
from scipy import stats

def task_func(animals, mean):
    # Generate a random number of customers following a Poisson distribution
    num_customers = stats.poisson.rvs(mu=mean, size=1)[0]
    
    # Initialize a dictionary to store the sales count for each animal type
    sales_summary = {animal: 0 for animal in animals}
    
    # Simulate sales for each customer
    for _ in range(num_customers):
        # Randomly select an animal type
        animal = random.choice(animals)
        # Increment the sales count for the selected animal type
        sales_summary[animal] += 1
    
    # Display the sales summary
    print("Sales Summary:")
    for animal, count in sales_summary.items():
        print(f"{animal}: {count}")
    
    # Return the sales summary as a dictionary
    return sales_summary
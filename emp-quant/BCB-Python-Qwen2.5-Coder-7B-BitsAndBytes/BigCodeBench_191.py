
import random
from scipy import stats

def task_func(animals, mean):
    # Generate the number of customers using Poisson distribution
    num_customers = stats.poisson.rvs(mu=mean)
    
    # Initialize a dictionary to store the count of each animal sold
    sales_summary = {animal: 0 for animal in animals}
    
    # Simulate each customer's purchase
    for _ in range(num_customers):
        # Randomly choose an animal from the list
        selected_animal = random.choice(animals)
        # Increment the count of the selected animal in the sales summary
        sales_summary[selected_animal] += 1
    
    # Display the sales summary
    print("Sales Summary:")
    for animal, count in sales_summary.items():
        print(f"{animal}: {count}")
    
    # Return the sales summary as a dictionary
    return sales_summary
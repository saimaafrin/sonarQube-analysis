import random
import math
def task_func(LETTERS=[chr(i) for i in range(97, 123)]):
    # Initialize the dictionary to store the results
    result = {}
    
    # Loop through each letter in the provided list
    for letter in LETTERS:
        # Generate a random list of integers between 0 and 100
        random_list = [random.randint(0, 100) for _ in range(random.randint(1, 10))]
        
        # Calculate the mean of the list
        mean = sum(random_list) / len(random_list)
        
        # Calculate the variance of the list
        variance = sum((x - mean) ** 2 for x in random_list) / len(random_list)
        
        # Calculate the population standard deviation
        std_dev = math.sqrt(variance)
        
        # Store the result in the dictionary
        result[letter] = std_dev
    
    # Return the dictionary containing the results
    return result
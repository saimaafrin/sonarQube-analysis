
import random
import math

def task_func(LETTERS=[chr(i) for i in range(97, 123)]):
    result = {}
    for letter in LETTERS:
        # Generate a list of random integers between 0 and 100
        random_integers = [random.randint(0, 100) for _ in range(random.randint(1, 10))]
        
        # Calculate the mean of the list
        mean = sum(random_integers) / len(random_integers)
        
        # Calculate the variance
        variance = sum((x - mean) ** 2 for x in random_integers) / len(random_integers)
        
        # Calculate the population standard deviation
        std_deviation = math.sqrt(variance)
        
        # Store the result in the dictionary
        result[letter] = std_deviation
    
    return result

import random
import bisect
import statistics
import matplotlib.pyplot as plt

def task_func(n, value):
    # Generate 'n' random numbers between 0 and 1
    numbers = [random.random() for _ in range(n)]
    
    # Calculate the average of the generated numbers
    average = statistics.mean(numbers)
    
    # Find numbers greater than the average
    greater_than_average = [num for num in numbers if num > average]
    
    # Count numbers greater than or equal to the specified value
    count_greater_or_equal = sum(1 for num in numbers if num >= value)
    
    # Sort the numbers
    sorted_numbers = sorted(numbers)
    
    # Output the results
    print(f"list: {greater_than_average}")
    print(f"int: {count_greater_or_equal}")
    
    # Plot the sorted numbers
    plt.figure(figsize=(8, 4))
    plt.plot(sorted_numbers, 'o')
    plt.title('Sorted Numbers')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.show()

import random
import bisect
import statistics
import matplotlib.pyplot as plt

def task_func(n, value):
    # Generate 'n' random numbers between 0 and 1
    numbers = [random.random() for _ in range(n)]
    
    # Calculate the average of all generated numbers
    average = statistics.mean(numbers)
    
    # Find numbers greater than the average
    greater_than_average = [num for num in numbers if num > average]
    
    # Count how many numbers are greater than or equal to the specified value
    count_greater_or_equal = sum(1 for num in numbers if num >= value)
    
    # Sort the numbers
    sorted_numbers = sorted(numbers)
    
    # Plot the sorted numbers
    plt.plot(sorted_numbers)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Sorted Random Numbers')
    plt.show()
    
    # Return the list and count
    return greater_than_average, count_greater_or_equal
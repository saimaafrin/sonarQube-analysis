import random
import statistics
AGE_RANGE = (22, 60)
def task_func(dict1):
    # Generate random ages for each employee within the range
    ages = [random.randint(AGE_RANGE[0], AGE_RANGE[1]) for _ in range(len(dict1))]

    # Calculate mean, median, and mode(s) of employee ages
    mean = statistics.mean(ages)
    median = statistics.median(ages)
    modes = statistics.mode(ages)

    # Return a tuple of mean, median, and a list of mode(s) of employee ages
    return (mean, median, modes)
dict1 = {
    "John": 25,
    "Jane": 30,
    "Bob": 35,
    "Alice": 28,
    "Eve": 32,
    "Mike": 38,
    "Lisa": 24,
    "Tom": 36,
    "Sarah": 27,
    "Edward": 34,
    "Emily": 30,
}
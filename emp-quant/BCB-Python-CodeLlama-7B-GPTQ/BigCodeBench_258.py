import json
import random
DATA = [
    {'name': 'John', 'age': 30, 'city': 'New York'},
    {'name': 'Peter', 'age': 35, 'city': 'London'},
    {'name': 'Susan', 'age': 25, 'city': 'Sydney'},
    {'name': 'Alice', 'age': 28, 'city': 'Paris'},
    {'name': 'Bob', 'age': 40, 'city': 'Tokyo'},
    {'name': 'Charlie', 'age': 22, 'city': 'Beijing'},
    {'name': 'David', 'age': 33, 'city': 'Mumbai'},
    {'name': 'Eve', 'age': 27, 'city': 'Berlin'},
    {'name': 'Frank', 'age': 32, 'city': 'Moscow'},
    {'name': 'Grace', 'age': 29, 'city': 'Rome'}
]
def task_func(utc_datetime, seed=0):
    """
    Select a random person from a dataset of people and their attributes (name, age, city) provided as a global variable DATA. Add a UTC timestamp to the person's data which is passed as an argument utc_datetime 'timestamp'. Finally, encode that person's data as a JSON string.
    """
    random.seed(seed)
    person = random.choice(DATA)
    person['timestamp'] = utc_datetime
    return json.dumps(person)
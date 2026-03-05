import random
from string import ascii_uppercase
def task_func(dict1):
    """
    Assign each employee of a company a unique ID based on their department code, consisting of the department code, followed by a random string of 5 letters.
    """
    # Initialize an empty list to store the unique employee IDs
    employee_ids = []

    # Iterate over the departments in the dictionary
    for department, employees in dict1.items():
        # Generate a random string of 5 letters
        random_string = ''.join(random.choice(ascii_uppercase) for _ in range(5))

        # Create a unique employee ID by concatenating the department code and the random string
        employee_id = f"{department}{random_string}"

        # Add the employee ID to the list
        employee_ids.append(employee_id)

    # Return the list of unique employee IDs
    return employee_ids
dict1 = {
    "IT": ["John", "Jane", "Bob"],
    "Sales": ["Alice", "Bob", "Charlie"],
    "HR": ["David", "Eve", "Frank"]
}
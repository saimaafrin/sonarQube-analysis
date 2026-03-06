import pandas as pd
from random import randint
def task_func(name: str, age: int, code: str, salary: float, bio: str) -> pd.DataFrame:
    """
    Generate a Pandas DataFrame of employees with their details based on the input provided.

    Parameters:
    - name (str): Name of the employee. This is case-sensitive. Must be one of the predefined
                  names: 'John', 'Alice', 'Bob', 'Charlie', 'David', otherwise the function raises
                  ValueError.
    - age (int): Age of the employee.
    - code (str): Code of the employee.
    - salary (float): Salary of the employee.
    - bio (str): Biography of the employee.

    Returns:
    data_df (pd.DataFrame): dataframe with columns: 'Name', 'Age', 'Code', 'Salary', 'Bio', 'Job Title'.
               The 'Job Title' is randomly assigned from the predefined job titles:
               'Engineer', 'Manager', 'Analyst', 'Developer', 'Tester'.

    Requirements:
    - pandas
    - random.randint

    Example:
    >>> random.seed(0)
    >>> df = task_func("John", 30, "A10B", 5000.0, "This is a bio with spaces")
    >>> print(df)
       Name  Age  Code  Salary                        Bio  Job Title
    0  John   30  A10B  5000.0  This is a bio with spaces  Developer
    """
    # TODO: Implement the function
    # Hint: Use the dictionary below to map the names to the job titles
    job_titles = {
        "John": "Developer",
        "Alice": "Manager",
        "Bob": "Analyst",
        "Charlie": "Engineer",
        "David": "Tester",
    }

    # Check if the name is in the dictionary
    if name not in job_titles:
        raise ValueError("Name not in dictionary")

    # Create a list of tuples with the data
    data = [
        (name, age, code, salary, bio, job_titles[name])
    ]

    # Create a dataframe from the list of tuples
    data_df = pd.DataFrame(data, columns=["Name", "Age", "Code", "Salary", "Bio", "Job Title"])

    return data_df
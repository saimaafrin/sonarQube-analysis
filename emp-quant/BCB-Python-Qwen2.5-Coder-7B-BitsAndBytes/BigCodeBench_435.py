
import pandas as pd
from random import choice

def task_func(name: str, age: int, code: str, salary: float, bio: str) -> pd.DataFrame:
    # Define possible job titles
    job_titles = ['Engineer', 'Manager', 'Analyst', 'Developer', 'Tester']
    
    # Randomly select a job title
    job_title = choice(job_titles)
    
    # Create a dictionary to hold employee details
    employee_details = {
        'Name': [name],
        'Age': [age],
        'Code': [code],
        'Salary': [salary],
        'Bio': [bio],
        'Job Title': [job_title]
    }
    
    # Convert the dictionary to a DataFrame
    data_df = pd.DataFrame(employee_details)
    
    return data_df
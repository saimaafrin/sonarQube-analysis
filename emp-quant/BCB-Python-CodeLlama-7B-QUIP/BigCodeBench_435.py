
import pandas as pd
from random import randint

def task_func(name: str, age: int, code: str, salary: float, bio: str) -> pd.DataFrame:
    job_titles = ['Engineer', 'Manager', 'Analyst', 'Developer', 'Tester']
    job_title = job_titles[randint(0, len(job_titles) - 1)]
    return pd.DataFrame({
        'Name': [name],
        'Age': [age],
        'Code': [code],
        'Salary': [salary],
        'Bio': [bio],
        'Job Title': [job_title]
    })
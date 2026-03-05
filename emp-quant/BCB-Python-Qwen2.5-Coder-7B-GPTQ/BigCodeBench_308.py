import pandas as pd
from statistics import mean
import random
FIELDS = ['Physics', 'Math', 'Chemistry', 'Biology', 'English', 'History']
STUDENTS = ['Student_' + str(i) for i in range(1, 101)]
def task_func(additional_fields = []):
    # Initialize a dictionary to store grades
    grades = {field: [] for field in FIELDS}
    
    # Populate the grades dictionary with random scores
    for _ in range(len(STUDENTS)):
        for field in FIELDS:
            grades[field].append(random.randint(0, 100))
    
    # Create a DataFrame from the grades dictionary
    df = pd.DataFrame(grades)
    
    # Calculate the average grade for each student
    df['Average'] = df.mean(axis=1)
    
    # Calculate the average grade for each subject
    average_grades = df.mean()
    
    # Add the average grades as a new row to the DataFrame
    df.loc['Average'] = average_grades
    
    # Rename the 'Average' column to 'Average Grade'
    df.rename(columns={'Average': 'Average Grade'}, inplace=True)
    
    return df
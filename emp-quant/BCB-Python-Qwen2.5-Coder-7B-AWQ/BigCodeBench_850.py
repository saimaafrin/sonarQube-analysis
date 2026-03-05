import pandas as pd
import statistics
import random
def task_func(students, subjects, seed=None):
    # Seed the random number generator for reproducibility
    if seed is not None:
        random.seed(seed)
    
    # Initialize a list to store student data
    student_data = []
    
    # Loop through each student
    for student in students:
        # Initialize a list to store grades for the current student
        grades = []
        
        # Loop through each subject and generate a random grade
        for subject in subjects:
            grade = random.randint(50, 100)  # Grades between 50 and 100
            grades.append(grade)
        
        # Calculate the average grade for the current student
        average_grade = statistics.mean(grades)
        
        # Append the student's data to the list
        student_data.append([student] + grades + [average_grade])
    
    # Create a DataFrame from the student data
    df = pd.DataFrame(student_data, columns=['Student'] + subjects + ['Average Grade'])
    
    return df
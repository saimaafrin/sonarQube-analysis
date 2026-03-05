import pandas as pd
import statistics
import random
def task_func(students, subjects, seed=None):
    if seed is not None:
        random.seed(seed)
    
    # Initialize a list to store student data
    student_data = []
    
    # Loop through each student
    for student in range(students):
        # Generate random grades for each subject
        grades = [random.randint(50, 100) for _ in range(subjects)]
        # Calculate the average grade
        average_grade = statistics.mean(grades)
        # Append the student's data to the list
        student_data.append([f'Student {student + 1}'] + grades + [average_grade])
    
    # Create a DataFrame from the student data
    df = pd.DataFrame(student_data, columns=['Student'] + [f'Subject{i + 1}' for i in range(subjects)] + ['Average Grade'])
    
    return df
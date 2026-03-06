
import pandas as pd
import statistics
import random

def task_func(students, subjects, seed=None):
    # Set the random seed if provided
    if seed is not None:
        random.seed(seed)

    # Create a list of grades for each student
    grades = []
    for student in students:
        student_grades = []
        for subject in subjects:
            grade = random.randint(0, 100)
            student_grades.append(grade)
        grades.append(student_grades)

    # Calculate the average grade for each student
    average_grades = []
    for student_grades in grades:
        average_grade = statistics.mean(student_grades)
        average_grades.append(average_grade)

    # Create a DataFrame with the results
    df = pd.DataFrame({
        'Student': students,
        'Subject1': grades[0],
        'Subject2': grades[1],
        'Subject3': grades[2],
        'Average Grade': average_grades
    })

    return df

df = task_func(students, subjects, seed)
print(df)

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def task_func(student_grades, possible_grades=["A", "B", "C", "D", "F"]):
    # Convert all grades to uppercase to ensure case-insensitivity
    student_grades = [grade.upper().strip() for grade in student_grades]
    
    # Filter out grades that are not in the possible grades list
    filtered_grades = [grade for grade in student_grades if grade in possible_grades]
    
    # Count the occurrences of each grade
    grade_counts = Counter(filtered_grades)
    
    # Create a DataFrame from the grade counts
    grade_df = pd.DataFrame(list(grade_counts.items()), columns=['Grade', 'Count'])
    grade_df.set_index('Grade', inplace=True)
    
    # Create a bar chart
    fig, ax = plt.subplots()
    grade_df['Count'].plot(kind='bar', ax=ax)
    ax.set_xlabel('Grade')
    ax.set_ylabel('Number of Students')
    ax.set_title('Grade Distribution')
    
    return grade_df, ax
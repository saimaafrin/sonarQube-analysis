import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
def task_func(student_grades, possible_grades=["A", "B", "C", "D", "F"]):
    # Convert student grades to uppercase and filter out non-possible grades
    filtered_grades = [grade.upper().strip() for grade in student_grades if grade.upper().strip() in possible_grades]
    
    # Count the occurrences of each grade
    grade_counts = Counter(filtered_grades)
    
    # Create a DataFrame from the grade counts
    grade_df = pd.DataFrame(list(grade_counts.items()), columns=['Grade', 'Count']).set_index('Grade')
    
    # Create a bar chart
    fig, ax = plt.subplots()
    grade_df['Count'].plot(kind='bar', ax=ax)
    ax.set_title('Grade Distribution')
    ax.set_xlabel('Grade')
    ax.set_ylabel('Number of Students')
    
    return grade_df, ax
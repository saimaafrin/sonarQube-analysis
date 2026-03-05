
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def task_func(student_grades, possible_grades=["A", "B", "C", "D", "F"]):
    # Normalize grades to uppercase and strip whitespace
    normalized_grades = [grade.strip().upper() for grade in student_grades]
    
    # Filter out grades not in possible grades
    valid_grades = [grade for grade in normalized_grades if grade in possible_grades]
    
    # Count the occurrences of each valid grade
    grade_counts = Counter(valid_grades)
    
    # Create a DataFrame from the grade counts
    grade_df = pd.DataFrame(list(grade_counts.items()), columns=['Grade', 'Count'])
    grade_df.set_index('Grade', inplace=True)
    
    # Create a bar chart
    fig, ax = plt.subplots()
    grade_df.plot(kind='bar', ax=ax)
    ax.set_xlabel('Grade')
    ax.set_ylabel('Number of Students')
    ax.set_title('Grade Distribution')
    
    return grade_df, ax
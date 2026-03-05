
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def task_func(student_grades, possible_grades=["A", "B", "C", "D", "F"]):
    # Convert grades to uppercase
    student_grades = [grade.upper() for grade in student_grades]

    # Create a Counter object to count the number of students in each grade
    grade_counts = Counter(student_grades)

    # Filter out grades that are not in the possible grades list
    grade_counts = {grade: count for grade, count in grade_counts.items() if grade in possible_grades}

    # Create a DataFrame with the grade counts
    grade_df = pd.DataFrame(grade_counts, index=["Grade Distribution"])

    # Create a bar chart plot
    fig, ax = plt.subplots()
    ax.bar(grade_df.index, grade_df["Count"])
    ax.set_xlabel("Grade")
    ax.set_ylabel("Number of Students")
    ax.set_title("Grade Distribution")

    return grade_df, ax

# Print the DataFrame
print(grade_df)

# Show the bar chart plot
plt.show()
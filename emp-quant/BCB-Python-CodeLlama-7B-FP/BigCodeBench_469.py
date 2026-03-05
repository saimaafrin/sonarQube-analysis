import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
def task_func(student_grades, possible_grades=["A", "B", "C", "D", "F"]):
    """
    Create a report on students' grades in a class, including a count of each grade out of all possible grades and a bar chart.
    Note: Grades are case-insensitive but whitespace-sensitive. Those not in possible grades are ignored.
    The function should output with:
        Tuple[DataFrame, Axes]:
        A pandas DataFrame with 'Grade' as the named index and their 'Count' as values.
        A bar chart plot (matplotlib's Axes object) visualizing 'Grade Distribution', with 'Grade' on the
        x-axis and 'Number of Students' on the y-axis.
    """
    # Create a dictionary to store the counts of each grade
    grade_counts = Counter()

    # Iterate over the student grades and update the counts
    for grade in student_grades:
        grade_counts[grade.strip().upper()] += 1

    # Create a DataFrame with the counts
    df = pd.DataFrame(grade_counts, index=["Grade Distribution"])

    # Create a bar chart plot
    fig, ax = plt.subplots()
    ax.bar(df.index, df.values)
    ax.set_xlabel("Grade")
    ax.set_ylabel("Number of Students")
    ax.set_title("Grade Distribution")

    return df, ax
student_grades = ["A", "B", "C", "D", "F", "a", "b", "c", "d", "f"]
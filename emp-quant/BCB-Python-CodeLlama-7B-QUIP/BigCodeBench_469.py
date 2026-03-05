
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def task_func(student_grades, possible_grades=["A", "B", "C", "D", "F"]):
    # Create a DataFrame with the counts of each grade
    grade_counts = Counter(student_grades)
    grade_df = pd.DataFrame(grade_counts, index=["Grade", "Count"])

    # Create a bar chart plot
    fig, ax = plt.subplots()
    ax.bar(grade_df.index, grade_df["Count"])
    ax.set_xlabel("Grade")
    ax.set_ylabel("Number of Students")
    ax.set_title("Grade Distribution")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    plt.show()

    return grade_df, fig
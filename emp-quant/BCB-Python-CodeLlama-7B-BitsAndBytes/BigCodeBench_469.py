
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def task_func(student_grades, possible_grades=["A", "B", "C", "D", "F"]):
    # Create a Counter object to count the number of students in each grade
    grade_counter = Counter(student_grades)

    # Filter out any grades that are not in the possible_grades list
    filtered_grades = [grade for grade in grade_counter if grade in possible_grades]

    # Create a DataFrame with the filtered grades and their counts
    grade_df = pd.DataFrame(filtered_grades, columns=["Grade"])
    grade_df["Count"] = grade_counter[filtered_grades]

    # Create a bar chart plot with the grade distribution
    fig, ax = plt.subplots()
    ax.bar(grade_df["Grade"], grade_df["Count"])
    ax.set_xlabel("Grade")
    ax.set_ylabel("Number of Students")
    ax.set_title("Grade Distribution")

    return grade_df, ax
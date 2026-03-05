import collections
import matplotlib.pyplot as plt
def task_func(data):
    """
    Combine a list of dictionaries with possibly differing keys (student names) into a single dictionary, calculate the average score for each student, and return a bar chart of average student scores with student on the x-axis and average score on the y-axis.
    This function handles data with varying dictionary lengths and missing keys by averaging available scores, ignoring None. If there is any negative score, the function raises ValueError. Bar colors can be: 'red', 'yellow', 'green', 'blue', 'purple'.
    The function should output with:
        ax (matplotlib.axes._axes.Axes or None): A bar chart showing the 'Average Student Scores', with
        'Student' on the x-axis and 'Average Score' on the y-axis.
        If data is empty, return None.
    """
    # Check if data is empty
    if not data:
        return None

    # Create a dictionary to store the average scores for each student
    student_scores = {}

    # Iterate over the list of dictionaries
    for student_dict in data:
        # Get the student name and scores
        student_name = student_dict['student']
        scores = student_dict['scores']

        # Calculate the average score for the student
        average_score = sum(scores) / len(scores)

        # Add the average score to the dictionary
        student_scores[student_name] = average_score

    # Create a bar chart of the average student scores
    fig, ax = plt.subplots()
    ax.bar(student_scores.keys(), student_scores.values(), color='blue')
    ax.set_xlabel('Student')
    ax.set_ylabel('Average Score')
    ax.set_title('Average Student Scores')

    return ax
data = [
    {'student': 'Alice', 'scores': [10, 8, 6, 4, 2]},
    {'student': 'Bob', 'scores': [8, 10, 6, 4, 2]},
    {'student': 'Charlie', 'scores': [10, 8, 6, 4, 2]},
    {'student': 'David', 'scores': [8, 10, 6, 4, 2]},
    {'student': 'Eve', 'scores': [10, 8, 6, 4, 2]},
]
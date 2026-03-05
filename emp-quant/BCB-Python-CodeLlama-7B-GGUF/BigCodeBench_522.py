
import collections
import matplotlib.pyplot as plt

def task_func(data):
    # Create a dictionary to store the average scores for each student
    student_scores = {}

    # Iterate over the list of dictionaries
    for student in data:
        # Get the student's name and scores
        student_name = student['name']
        student_scores = student['scores']

        # Calculate the average score for the student
        average_score = sum(student_scores) / len(student_scores)

        # Add the average score to the dictionary
        student_scores[student_name] = average_score

    # Create a bar chart of the average scores
    ax = plt.bar(student_scores.keys(), student_scores.values())

    # Set the x-axis labels
    ax.set_xticks(student_scores.keys())
    ax.set_xticklabels(student_scores.keys())

    # Set the y-axis labels
    ax.set_yticks(student_scores.values())
    ax.set_yticklabels(student_scores.values())

    # Set the title of the chart
    ax.set_title('Average Student Scores')

    # Set the color of the bars
    ax.set_color('red')

    # Return the bar chart
    return ax
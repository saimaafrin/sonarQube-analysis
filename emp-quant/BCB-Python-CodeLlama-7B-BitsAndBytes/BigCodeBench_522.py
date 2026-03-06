
import collections
import matplotlib.pyplot as plt

def task_func(data):
    # Create a dictionary to store the average scores for each student
    student_scores = {}

    # Iterate over the list of dictionaries and calculate the average score for each student
    for student in data:
        # Get the student's name and scores
        student_name = student['name']
        scores = student['scores']

        # Calculate the average score for this student
        average_score = sum(scores) / len(scores)

        # Add the average score to the dictionary
        student_scores[student_name] = average_score

    # Create a bar chart of the average scores
    ax = plt.bar(student_scores.keys(), student_scores.values(), color='blue')

    # Set the x-axis and y-axis labels
    ax.set_xlabel('Student')
    ax.set_ylabel('Average Score')

    # Return the bar chart
    return ax

# Call the function with the sample data
ax = task_func(data)

# Show the bar chart
plt.show()
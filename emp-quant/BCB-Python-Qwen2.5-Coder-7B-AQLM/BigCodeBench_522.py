
import collections
import matplotlib.pyplot as plt

def task_func(data):
    if not data:
        return None

    # Initialize a dictionary to store the total scores and count of scores for each student
    total_scores = collections.defaultdict(float)
    count_scores = collections.defaultdict(int)

    # Iterate over each dictionary in the list
    for student_scores in data:
        for student, score in student_scores.items():
            if score is None:
                continue
            if score < 0:
                raise ValueError("Negative score found")
            total_scores[student] += score
            count_scores[student] += 1

    # Calculate the average scores
    average_scores = {student: total_scores[student] / count_scores[student] for student in total_scores}

    # Define the bar colors
    colors = ['red', 'yellow', 'green', 'blue', 'purple']

    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(average_scores.keys(), average_scores.values(), color=colors[:len(average_scores)])

    # Set the labels and title
    ax.set_xlabel('Student')
    ax.set_ylabel('Average Score')
    ax.set_title('Average Student Scores')

    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45)

    # Return the axes object
    return ax
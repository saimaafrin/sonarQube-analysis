import collections
import matplotlib.pyplot as plt
def task_func(data):
    if not data:
        return None

    # Initialize a dictionary to store the total scores and count of scores for each student
    student_scores = collections.defaultdict(list)

    # Iterate over each dictionary in the list
    for student_data in data:
        for student, score in student_data.items():
            if score is None:
                continue
            if score < 0:
                raise ValueError("Negative score found")
            student_scores[student].append(score)

    # Calculate the average score for each student
    average_scores = {student: sum(scores) / len(scores) for student, scores in student_scores.items()}

    # Prepare data for plotting
    students = list(average_scores.keys())
    scores = list(average_scores.values())

    # Define a list of colors for the bar chart
    colors = ['red', 'yellow', 'green', 'blue', 'purple']

    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(students, scores, color=colors[:len(students)])

    # Set labels and title
    ax.set_xlabel('Student')
    ax.set_ylabel('Average Score')
    ax.set_title('Average Student Scores')

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

    # Return the axes object
    return ax
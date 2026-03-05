import collections
import matplotlib.pyplot as plt
def task_func(data):
    if not data:
        return None

    # Initialize a dictionary to store the total scores and count of scores for each student
    total_scores = collections.defaultdict(float)
    score_counts = collections.defaultdict(int)

    # Iterate over each dictionary in the list
    for student_scores in data:
        for student, score in student_scores.items():
            if score is None:
                continue
            if score < 0:
                raise ValueError("Negative score found")
            total_scores[student] += score
            score_counts[student] += 1

    # Calculate the average scores
    average_scores = {student: total_scores[student] / score_counts[student] for student in total_scores}

    # Prepare data for plotting
    students = list(average_scores.keys())
    scores = list(average_scores.values())

    # Define a list of colors
    colors = ['red', 'yellow', 'green', 'blue', 'purple']

    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(students, scores, color=colors[:len(students)])

    # Set labels and title
    ax.set_xlabel('Student')
    ax.set_ylabel('Average Score')
    ax.set_title('Average Student Scores')

    return ax
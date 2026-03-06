
import collections
import matplotlib.pyplot as plt

def task_func(data):
    if not data:
        return None
    
    # Combine all dictionaries into one
    combined_scores = collections.defaultdict(list)
    for student_scores in data:
        for student, score in student_scores.items():
            if score is not None and score >= 0:
                combined_scores[student].append(score)
    
    # Calculate average scores
    average_scores = {student: sum(scores) / len(scores) for student, scores in combined_scores.items()}
    
    # Prepare data for plotting
    students = list(average_scores.keys())
    scores = list(average_scores.values())
    
    # Define color mapping
    colors = ['red', 'yellow', 'green', 'blue', 'purple']
    
    # Create bar chart
    fig, ax = plt.subplots()
    ax.bar(students, scores, color=colors[:len(students)])
    
    # Set labels and title
    ax.set_xlabel('Student')
    ax.set_ylabel('Average Score')
    ax.set_title('Average Student Scores')
    
    return ax
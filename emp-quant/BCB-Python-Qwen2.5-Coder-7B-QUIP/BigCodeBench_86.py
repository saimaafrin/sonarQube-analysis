
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(students=["Alice", "Bob", "Charlie", "David", "Eve"], seed=42):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate random scores for the students
    scores = np.random.randint(0, 100, size=len(students))
    
    # Create a DataFrame with students and their scores
    df = pd.DataFrame({'Student': students, 'Score': scores})
    
    # Sort the DataFrame by the scores
    df = df.sort_values(by='Score')
    
    # Create a bar plot of the scores
    fig, ax = plt.subplots()
    df.plot(kind='bar', x='Student', y='Score', ax=ax)
    ax.set_xlabel('Student')
    ax.set_ylabel('Score')
    ax.set_title('Student Scores')
    
    # Return the sorted DataFrame and the Axes object
    return df, ax
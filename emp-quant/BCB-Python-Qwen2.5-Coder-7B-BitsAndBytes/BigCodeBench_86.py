
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(students=["Alice", "Bob", "Charlie", "David", "Eve"], seed=42):
    # Set the seed for reproducibility
    np.random.seed(seed)
    
    # Generate random scores for each student
    scores = np.random.randint(0, 100, size=len(students))
    
    # Create a DataFrame with students and their scores
    df = pd.DataFrame({'Student': students, 'Score': scores})
    
    # Sort the DataFrame by scores in ascending order
    df_sorted = df.sort_values(by='Score')
    
    # Plotting the bar chart
    fig, ax = plt.subplots()
    ax.bar(df_sorted['Student'], df_sorted['Score'])
    ax.set_xlabel('Students')
    ax.set_ylabel('Scores')
    ax.set_title('Student Scores')
    
    return df_sorted, ax
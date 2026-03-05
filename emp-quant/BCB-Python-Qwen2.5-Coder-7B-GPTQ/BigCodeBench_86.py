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
    
    # Create a bar plot of the scores
    fig, ax = plt.subplots()
    ax.bar(df_sorted['Student'], df_sorted['Score'], color='blue')
    ax.set_xlabel('Student')
    ax.set_ylabel('Score')
    ax.set_title('Student Scores')
    
    return df_sorted, ax
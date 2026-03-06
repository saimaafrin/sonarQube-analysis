
import pandas as pd
from collections import Counter

def task_func(data):
    # Check if the required keys are present in the dictionary
    required_keys = {'Name', 'Age', 'Score'}
    if not required_keys.issubset(data.keys()):
        raise ValueError("Dictionary must contain 'Name', 'Age', and 'Score' keys.")
    
    # Create a list of dictionaries from the input dictionary
    students = [{'Name': name, 'Age': age, 'Score': score} for name, age, score in zip(data['Name'], data['Age'], data['Score'])]
    
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(students)
    
    # Sort the DataFrame by 'Name' and 'Age'
    df_sorted = df.sort_values(by=['Name', 'Age'])
    
    # Calculate the average score per student
    avg_scores = df_sorted.groupby('Name')['Score'].mean()
    
    # Find the most common age
    age_counts = Counter(df_sorted['Age'])
    most_common_age = age_counts.most_common(1)[0][0] if age_counts else None
    
    return df_sorted, avg_scores, most_common_age
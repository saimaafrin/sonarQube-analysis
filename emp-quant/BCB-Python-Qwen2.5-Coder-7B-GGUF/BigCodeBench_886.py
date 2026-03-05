
import pandas as pd
from collections import Counter

def task_func(data):
    required_keys = {'Name', 'Age', 'Score'}
    if not required_keys.issubset(data.keys()):
        raise ValueError("The dictionary does not have the required keys.")
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Sort DataFrame by 'Name' and 'Age'
    df_sorted = df.sort_values(by=['Name', 'Age'])
    
    # Calculate average score per student
    avg_scores = df_sorted.groupby('Name')['Score'].mean()
    
    # Find the most common age
    age_counts = Counter(df_sorted['Age'])
    most_common_age = age_counts.most_common(1)
    most_common_age = most_common_age[0][0] if most_common_age else None
    
    return df_sorted, avg_scores, most_common_age
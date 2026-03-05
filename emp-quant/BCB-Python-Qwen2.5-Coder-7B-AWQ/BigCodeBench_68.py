import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(data='/path/to/data.csv', emp_prefix='EMP'):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(data)
    
    # Filter the lines where the employee ID begins with the specified prefix
    filtered_df = df[df['Employee ID'].str.startswith(emp_prefix)]
    
    # Draw a histogram of the age
    plt.figure(figsize=(10, 6))
    ax = sns.histplot(filtered_df['Age'], kde=True)
    plt.title(f'Histogram of Age for Employee IDs starting with {emp_prefix}')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    
    return filtered_df, ax
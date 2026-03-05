
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data='/path/to/data.csv', emp_prefix='EMP'):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(data)
    
    # Filter the lines where the employee ID begins with the specified prefix
    filtered_df = df[df['Employee ID'].str.startswith(emp_prefix)]
    
    # Draw a histogram of the 'Age' column of the filtered data
    plt.figure(figsize=(10, 6))
    sns.histplot(filtered_df['Age'], bins=10, kde=True)
    plt.title(f'Histogram of Age for Employee IDs starting with {emp_prefix}')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()
    
    return filtered_df, plt.gca()
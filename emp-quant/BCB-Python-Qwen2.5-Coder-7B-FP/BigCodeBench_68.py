import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(data='/path/to/data.csv', emp_prefix='EMP'):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(data)
    
    # Filter the lines where the employee ID begins with the specified prefix
    filtered_df = df[df['Employee ID'].str.startswith(emp_prefix)]
    
    # Draw a histogram of the 'Age' column of the filtered data
    ax = sns.histplot(filtered_df['Age'], kde=True)
    
    # Set the title and labels for the plot
    ax.set_title(f'Histogram of Age for Employees with ID starting with {emp_prefix}')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    
    # Return the DataFrame and the Axes object
    return filtered_df, ax
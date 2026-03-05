import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(data='/path/to/data.csv', emp_prefix='EMP'):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(data)
    
    # Filter the lines in which the employee ID begins with a prefix
    filtered_df = df[df['Employee ID'].str.startswith(emp_prefix)]
    
    # Draw a histogram of its age
    ax = sns.histplot(filtered_df['Age'], kde=True)
    
    # Set the title and labels
    ax.set_title('Age Distribution of Employees with ID Prefix')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    
    # Return the DataFrame and the Axes object
    return filtered_df, ax
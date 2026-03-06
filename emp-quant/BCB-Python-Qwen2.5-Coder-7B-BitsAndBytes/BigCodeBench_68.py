
import pandas as pd
import seaborn as sns

def task_func(data='/path/to/data.csv', emp_prefix='EMP'):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(data)
    
    # Filter the lines where the employee ID starts with the specified prefix
    filtered_df = df[df['Employee ID'].str.startswith(emp_prefix)]
    
    # Draw a histogram of the 'Age' column of the filtered data
    axes = sns.histplot(filtered_df['Age'], kde=False)
    
    return filtered_df, axes
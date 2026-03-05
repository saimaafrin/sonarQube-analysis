
import pandas as pd
import seaborn as sns

def task_func(data='/path/to/data.csv', emp_prefix='EMP'):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(data)
    
    # Filter the DataFrame to include only rows where the 'Employee ID' starts with the given prefix
    df_filtered = df[df['Employee ID'].str.startswith(emp_prefix)]
    
    # Draw a histogram of the 'Age' column of the filtered data
    ax = sns.histplot(df_filtered['Age'], kde=True)
    
    # Return the filtered DataFrame and the Axes object
    return df_filtered, ax

import pandas as pd
import seaborn as sns

def task_func(data='/path/to/data.csv', emp_prefix='EMP'):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(data)

    # Filter the lines in which the employee ID begins with the prefix
    df = df[df['Employee ID'].str.startswith(emp_prefix)]

    # Draw a histogram of the 'Age' column of the filtered data
    sns.histplot(data=df, x='Age')

    # Return the filtered DataFrame
    return df

# Call the function and print the output
df = task_func(data='/path/to/data.csv', emp_prefix='EMP')
print(df)
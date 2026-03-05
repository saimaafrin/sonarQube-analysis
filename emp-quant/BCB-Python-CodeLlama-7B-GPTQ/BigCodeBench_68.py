import pandas as pd
import seaborn as sns
def task_func(data='/path/to/data.csv', emp_prefix='EMP'):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(data)

    # Filter the lines in which the employee ID begins with the prefix
    df = df[df['Employee ID'].str.startswith(emp_prefix)]

    # Draw a histogram of the 'Age' column of the filtered data
    sns.histplot(df['Age'])

    # Return the filtered DataFrame and the histogram plot
    return df, sns.histplot(df['Age'])
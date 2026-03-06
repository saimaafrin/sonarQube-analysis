
import bisect
import statistics
import matplotlib.pyplot as plt

def task_func(df, column, value):
    # Check if the column exists in the DataFrame
    if column not in df.columns:
        raise ValueError("Column does not exist in the DataFrame")
    
    # Check if the value is a number
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a number")
    
    # Calculate the average of the column
    avg = df[column].mean()
    
    # Find values greater than the average
    greater_than_avg = df[df[column] > avg][column].values
    
    # Count the number of values greater than the given value
    count_greater_than_value = sum(1 for x in df[column] if x > value)
    
    # Plot a histogram of the column
    fig, ax = plt.subplots()
    df[column].hist(ax=ax)
    
    return greater_than_avg, count_greater_than_value, ax
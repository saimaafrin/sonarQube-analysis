import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
def task_func(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame")
    
    # Remove rows with duplicate names
    df = df.drop_duplicates(subset='name')
    
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(df['age'], df['score'])
    
    # Create scatter plot
    plt.scatter(df['age'], df['score'], color='blue', label='Data points')
    
    # Create regression line
    regression_line = slope * df['age'] + intercept
    plt.plot(df['age'], regression_line, color='red', label='Regression line')
    
    # Set plot title and labels
    plt.title('Linear Regression')
    plt.xlabel('Age')
    plt.ylabel('Score')
    
    # Add legend
    plt.legend()
    
    # Return the matplotlib.pyplot object and the axes object
    return plt, plt.gca()
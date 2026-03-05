
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame.")
    
    # Remove duplicate names
    df = df.drop_duplicates(subset='name')
    
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(df['age'], df['score'])
    
    # Plot the regression line and scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df['age'], df['score'], color='blue', label='Data')
    ax.plot(df['age'], df['score'], color='red', label='Regression Line')
    
    # Set plot title and labels
    ax.set_title('Linear Regression')
    ax.set_xlabel('Age')
    ax.set_ylabel('Score')
    
    # Show legend
    ax.legend()
    
    return (fig, ax)
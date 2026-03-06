
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    
    # Remove duplicates based on 'name' column
    df = df.drop_duplicates(subset='name')
    
    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = stats.linregress(df['age'], df['score'])
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Plot the scatter plot
    ax.scatter(df['age'], df['score'], color='blue', label='Data points')
    
    # Plot the regression line
    x_vals = np.array(ax.get_xlim())
    y_vals = intercept + slope * x_vals
    ax.plot(x_vals, y_vals, '--r', label='Regression line')
    
    # Set labels and title
    ax.set_xlabel('Age')
    ax.set_ylabel('Score')
    ax.set_title('Linear Regression')
    
    # Show legend
    ax.legend()
    
    return fig, ax
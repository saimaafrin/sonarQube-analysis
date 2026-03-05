import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(data=None):
    """
    Converts string-formatted weights to floats and plots a scatter plot of weight against height.
    
    Parameters:
    - data (dict, optional): A dictionary with keys 'Weight_String' and 'Height'. 
      'Weight_String' should contain a list of weight values in string format, 
      while 'Height' should have a list of corresponding height values in numerical format.
      If not provided, a default dataset is used.
    
    Returns:
    - ax (matplotlib.axes._axes.Axes): A scatter plot with weight on the x-axis and height on the y-axis, titled "Weight vs Height".
    
    Raises:
    - ValueError: If any of the values in the 'Weight_String' key are not formatted as strings.
    """
    # Default dataset if no data is provided
    if data is None:
        data = {
            'Weight_String': ['50', '60', '70', '80', '90'],
            'Height': [150, 160, 170, 180, 190]
        }
    
    # Convert string-formatted weights to float
    try:
        data['Weight'] = [float(weight) for weight in data['Weight_String']]
    except ValueError as e:
        raise ValueError("All values in 'Weight_String' must be formatted as strings.") from e
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    
    # Plot a scatter plot
    ax = sns.scatterplot(x='Weight', y='Height', data=df)
    ax.set_title('Weight vs Height')
    
    return ax
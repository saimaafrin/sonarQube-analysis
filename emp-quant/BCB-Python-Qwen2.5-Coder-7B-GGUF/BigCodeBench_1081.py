
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data=None):
    # Default dataset if no data is provided
    if data is None:
        data = {
            'Weight_String': ['50', '60', '70', '80', '90'],
            'Height': [150, 160, 170, 180, 190]
        }
    
    # Convert string-formatted weights to floats
    try:
        data['Weight'] = [float(weight) for weight in data['Weight_String']]
    except ValueError:
        raise ValueError("All values in 'Weight_String' must be formatted as strings.")
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    
    # Plotting the scatter plot
    ax = sns.scatterplot(x='Weight', y='Height', data=df)
    ax.set_title('Weight vs Height')
    
    return ax
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(data=None):
    # Default dataset if no data is provided
    if data is None:
        data = {
            'Weight_String': ['70.5', '65.0', '75.2', '80.3', '68.1'],
            'Height': [175, 168, 180, 185, 170]
        }
    
    # Check if 'Weight_String' values are all strings
    if not all(isinstance(weight, str) for weight in data['Weight_String']):
        raise ValueError("All values in 'Weight_String' must be strings.")
    
    # Convert 'Weight_String' to float
    data['Weight'] = [float(weight) for weight in data['Weight_String']]
    
    # Create a scatter plot
    ax = sns.scatterplot(x='Weight', y='Height', data=data)
    ax.set_title('Weight vs Height')
    
    return ax
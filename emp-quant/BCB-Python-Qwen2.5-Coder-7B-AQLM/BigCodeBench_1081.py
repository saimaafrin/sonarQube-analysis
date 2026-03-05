
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data=None):
    if data is None:
        data = {
            'Weight_String': ['70', '75', '80', '85', '90'],
            'Height': [170, 175, 180, 185, 190]
        }
    
    # Validate the 'Weight_String' key
    if not all(isinstance(weight, str) for weight in data['Weight_String']):
        raise ValueError("All values in 'Weight_String' must be strings.")
    
    # Convert string weights to float
    data['Weight'] = [float(weight) for weight in data['Weight_String']]
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    
    # Plot the scatter plot
    ax = sns.scatterplot(x='Weight', y='Height', data=df)
    ax.set_title('Weight vs Height')
    
    return ax

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data=None):
    if data is None:
        # Default dataset
        data = {
            'Weight_String': ['70kg', '65kg', '80kg', '75kg', '90kg'],
            'Height': [170, 165, 180, 175, 190]
        }
    
    # Convert string weights to float
    try:
        data['Weight'] = [float(weight.strip('kg')) for weight in data['Weight_String']]
    except ValueError:
        raise ValueError("All values in 'Weight_String' must be formatted as strings.")
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Plotting
    ax = sns.scatterplot(x='Weight', y='Height', data=df)
    ax.set_title('Weight vs Height')
    
    return ax
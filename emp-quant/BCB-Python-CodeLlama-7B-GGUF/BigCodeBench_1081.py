
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data=None):
    # Check if data is provided
    if data is None:
        # Use default dataset if not provided
        data = {'Weight_String': ['70.0', '68.0', '72.0', '65.0', '75.0'],
                'Height': [170, 168, 172, 165, 175]}

    # Convert string-formatted weights to floats
    data['Weight'] = data['Weight_String'].astype(float)

    # Remove 'Weight_String' key from dictionary
    del data['Weight_String']

    # Create scatter plot
    ax = sns.scatterplot(data=data, x='Weight', y='Height', title='Weight vs Height')

    # Return scatter plot
    return ax
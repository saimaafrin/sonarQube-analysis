
import pandas as pd
import seaborn as sns

def task_func(data=None):
    # Check if the input data is provided
    if data is None:
        # Use a default dataset if no data is provided
        data = {'Weight_String': ['70', '65', '72', '60', '68', '75', '73', '65', '70', '68'],
                'Height': [170, 165, 172, 160, 168, 175, 173, 165, 170, 168]}

    # Convert the weight values to floats
    data['Weight'] = data['Weight_String'].apply(float)

    # Create a scatter plot with weight on the x-axis and height on the y-axis
    ax = sns.scatterplot(x='Weight', y='Height', data=data)

    # Set the title of the plot
    ax.set_title('Weight vs Height')

    # Return the plot
    return ax
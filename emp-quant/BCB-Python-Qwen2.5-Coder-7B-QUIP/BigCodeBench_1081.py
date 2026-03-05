
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data=None):
    # Default dataset if none provided
    if data is None:
        data = {
            'Weight_String': ['60', '70', '75', '80', '85'],
            'Height': [160, 170, 175, 180, 185]
        }

    # Check if 'Weight_String' contains strings and 'Height' contains numbers
    if not all(isinstance(weight, str) for weight in data['Weight_String']):
        raise ValueError("All values in 'Weight_String' must be strings.")
    if not all(isinstance(height, (int, float)) for height in data['Height']):
        raise ValueError("All values in 'Height' must be numbers.")

    # Convert 'Weight_String' to float
    data['Weight'] = pd.to_numeric(data['Weight_String'], errors='raise')

    # Plotting the scatter plot
    fig, ax = plt.subplots()
    sns.scatterplot(x='Weight', y='Height', data=data, ax=ax)
    ax.set_title('Weight vs Height')

    return ax
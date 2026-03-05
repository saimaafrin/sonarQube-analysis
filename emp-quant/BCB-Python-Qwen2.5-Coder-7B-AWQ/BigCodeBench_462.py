import pandas as pd
import random
import matplotlib.pyplot as plt
def task_func(num_rows=100, categories=["a", "b", "c", "d", "e"], random_seed=42):
    """
    Generates a DataFrame with random category and integer values, and plots a bar chart of category counts.

    Parameters:
    num_rows (int): The number of rows in the DataFrame. Must be greater than 0.
    categories (list): A list of category strings.
    random_seed (int): The seed for the random number generator.

    Returns:
    pd.DataFrame: A pandas DataFrame with randomly generated category data.
    matplotlib.pyplot.Axes: A bar chart visualizing the category counts.
    """
    if num_rows < 1:
        raise ValueError("num_rows must be greater than 0")

    # Set the random seed for reproducibility
    random.seed(random_seed)

    # Generate random data
    data = {
        'category': [random.choice(categories) for _ in range(num_rows)],
        'value': [random.randint(1, 100) for _ in range(num_rows)]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Plot bar chart
    ax = df['category'].value_counts().plot(kind='bar')
    ax.set_title('Category Counts')

    return df, ax
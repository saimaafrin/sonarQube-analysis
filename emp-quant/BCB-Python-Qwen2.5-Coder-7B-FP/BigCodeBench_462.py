import pandas as pd
import random
import matplotlib.pyplot as plt
def task_func(num_rows=100, categories=["a", "b", "c", "d", "e"], random_seed=42):
    """
    Generates a DataFrame with specified number of rows, each containing a randomly selected category
    from the provided categories list and a random integer between 1 and 100. Also generates a bar chart
    visualizing the counts of each category in the DataFrame.

    Parameters:
    - num_rows (int): The number of rows in the DataFrame. Must be at least 1.
    - categories (list): A list of category names to choose from.
    - random_seed (int): Seed for the random number generator for reproducibility.

    Returns:
    - pd.DataFrame: A pandas DataFrame with randomly generated category data.
    - matplotlib.pyplot.Axes: A bar chart visualizing the category counts.
    """
    if num_rows < 1:
        raise ValueError("num_rows must be at least 1")

    # Set the random seed for reproducibility
    random.seed(random_seed)

    # Generate random data
    data = {
        'Category': [random.choice(categories) for _ in range(num_rows)],
        'Value': [random.randint(1, 100) for _ in range(num_rows)]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Generate bar chart
    ax = df['Category'].value_counts().plot(kind='bar')
    ax.set_title('Category Counts')

    return df, ax
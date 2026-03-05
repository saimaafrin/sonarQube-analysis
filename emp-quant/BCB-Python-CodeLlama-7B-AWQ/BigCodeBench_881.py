import pandas as pd
import random
def task_func(csv_file, column_name='data', pattern='\d+[xX]', sample_size=None, seed=42):
    """
    Search for matches with a specified regex pattern in a given column of a CSV file and optionally return a random sample of these matches.

    Args:
        csv_file (str): Path to the CSV file.
        column_name (str, optional): Name of the column to search in. Defaults to 'data'.
        pattern (str, optional): Regex pattern to search for. Defaults to '\d+[xX]'.
        sample_size (int, optional): Number of random samples to return. Defaults to None.
        seed (int, optional): Random seed for reproducibility. Defaults to 42.

    Returns:
        DataFrame: A pandas DataFrame containing either all the rows with matches or a random sample of them.
    """
    # Load the CSV file
    df = pd.read_csv(csv_file)

    # Extract the column to search in
    column = df[column_name]

    # Create a list of indices for the rows that match the pattern
    indices = []
    for i, row in enumerate(column):
        if re.search(pattern, row):
            indices.append(i)

    # If a sample size is specified, generate a random sample of indices
    if sample_size:
        random.seed(seed)
        indices = random.sample(indices, sample_size)

    # Return the DataFrame with the selected rows
    return df.iloc[indices]
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt
import os
def task_func(file_path='arena.csv', target_column='Index', seed=42):
    """Trains a random forest model on data from a CSV file, using one column as the target variable (y) and the rest as features (X), and visualizes the feature importances in a bar plot.

    Args:
        file_path (str): Path to the CSV file.
        target_column (str): Name of the target column.
        seed (int, optional): Random seed for reproducibility. Defaults to 42.

    Returns:
        matplotlib.axes.Axes: Axes object displaying the bar plot of feature importances.
        numpy.ndarray: Array containing the feature importances derived from the random forest model.

    Raises:
        FileNotFoundError: Raised if the specified file_path does not lead to a valid file.
        ValueError: Raised if the specified target_column is not found in the CSV file's columns, or if the input data contains NaN, infinity or a value too large for dtype('float32').
    """
    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"{file_path} does not lead to a valid file.")

    # Load the data
    df = pd.read_csv(file_path)

    # Check if the target column exists
    if target_column not in df.columns:
        raise ValueError(f"{target_column} is not found in the CSV file's columns.")

    # Drop rows with missing values
    df.dropna(inplace=True)

    # Split the data into features and target
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Train a random forest model
    model = RandomForestClassifier(n_estimators=100, random_state=seed)
    model.fit(X, y)

    # Get the feature importances
    importances = model.feature_importances_

    # Plot the feature importances
    ax = sns.barplot(x=X.columns, y=importances)

    return ax, importances
file_path = 'arena.csv'
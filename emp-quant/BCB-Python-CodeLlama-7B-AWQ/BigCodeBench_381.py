import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt
import os
def task_func(file_path='arena.csv', target_column='Index', seed=42):
    """
    Trains a random forest model on data from a CSV file, using one column as the target variable (y) and the rest as features (X), and visualizes the feature importances in a bar plot.
    This function also handles missing values by dropping rows with any NaN values.
    """
    # Check if the specified file_path leads to a valid file
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"{file_path} does not lead to a valid file.")

    # Check if the specified target_column is found in the CSV file's columns
    if target_column not in pd.read_csv(file_path).columns:
        raise ValueError(f"{target_column} is not found in the CSV file's columns.")

    # Load the data
    data = pd.read_csv(file_path)

    # Drop rows with any NaN values
    data.dropna(inplace=True)

    # Split the data into features and target
    X = data.drop(columns=[target_column])
    y = data[target_column]

    # Train a random forest model predicting the target column from the features
    model = RandomForestClassifier(n_estimators=100, random_state=seed)
    model.fit(X, y)

    # Get the feature importances
    importances = model.feature_importances_

    # Plot the feature importances
    ax = sns.barplot(x=importances.index, y=importances.values)

    return ax, importances
file_path = 'arena.csv'

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt
import os

def task_func(file_path='arena.csv', target_column='Index', seed=42):
    # Check if file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist")

    # Load data from CSV file
    df = pd.read_csv(file_path)

    # Check if target column is present in data
    if target_column not in df.columns:
        raise ValueError(f"Target column {target_column} not found in data")

    # Drop rows with missing values
    df.dropna(inplace=True)

    # Split data into features and target
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Train random forest model
    rf = RandomForestClassifier(n_estimators=100, random_state=seed)
    rf.fit(X, y)

    # Get feature importances
    importances = rf.feature_importances_

    # Plot feature importances
    ax = sns.barplot(x=X.columns, y=importances)

    return ax, importances
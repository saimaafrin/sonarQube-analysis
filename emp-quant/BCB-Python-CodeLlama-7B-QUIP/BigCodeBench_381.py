
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt
import os

def task_func(file_path='arena.csv', target_column='Index', seed=42):
    # Load the data
    df = pd.read_csv(file_path)

    # Drop rows with any NaN values
    df.dropna(inplace=True)

    # Split the data into features and target variable
    X = df.drop(target_column, axis=1)
    y = df[target_column]

    # Train a random forest model
    model = RandomForestClassifier(seed=seed)
    model.fit(X, y)

    # Get the feature importances
    importances = model.feature_importances_

    # Plot the feature importances
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(importances, ax=ax)
    ax.set_xlabel('Feature Importance')
    ax.set_ylabel('Feature')
    ax.set_title('Feature Importances')
    plt.show()

    return ax, importances
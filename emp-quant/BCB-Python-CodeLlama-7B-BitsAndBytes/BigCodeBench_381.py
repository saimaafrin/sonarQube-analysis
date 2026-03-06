
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt
import os

def task_func(file_path='arena.csv', target_column='Index', seed=42):
    # Load the data from the CSV file
    df = pd.read_csv(file_path)

    # Drop any rows with missing values
    df.dropna(inplace=True)

    # Split the data into features and target variable
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Train a random forest model on the data
    clf = RandomForestClassifier(n_estimators=100, random_state=seed)
    clf.fit(X, y)

    # Get the feature importances
    importances = clf.feature_importances_

    # Plot the feature importances
    ax = sns.barplot(x=X.columns, y=importances)

    # Return the axes object and the feature importances
    return ax, importances

# Create a dummy file for testing
create_dummy_file('arena.csv')

# Train a random forest model and plot the feature importances
ax, importances = task_func('arena.csv', 'Index')

# Remove the dummy file
os.remove('arena.csv')
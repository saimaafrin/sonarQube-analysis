
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def task_func(df, target_column):
    # Initialize the RandomForestClassifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Train the classifier
    clf.fit(df, df[target_column])
    
    # Get the feature importances
    feature_importances = clf.feature_importances_
    
    # Sort the feature importances and feature names
    feature_importances_sorted = feature_importances.argsort()[::-1]
    feature_names_sorted = df.columns[feature_importances_sorted]
    
    # Plot the bar plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x=feature_importances_sorted, y=feature_names_sorted, orient='h')
    plt.xlabel('Feature Importance Score')
    plt.ylabel('Features')
    plt.title('Visualizing Important Features')
    plt.show()
    
    return clf, plt.gca()
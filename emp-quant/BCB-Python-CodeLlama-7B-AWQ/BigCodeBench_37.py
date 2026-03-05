import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df, target_column):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df.drop(target_column, axis=1), df[target_column], test_size=0.2, random_state=42)

    # Train a random forest classifier on the training data
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Plot the feature importances
    feature_importances = clf.feature_importances_
    feature_names = X_train.columns
    sorted_importances = sorted(zip(feature_importances, feature_names), key=lambda x: x[0], reverse=True)

    # Plot the bar plot
    sns.barplot(x=sorted_importances[:, 0], y=sorted_importances[:, 1], xlabel='Feature Importance Score', ylabel='Features', title='Visualizing Important Features')

    # Return the random forest classifier and the Axes object of the plotted data
    return clf, plt.gca()
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10], 'C': [3, 6, 9, 12, 15], 'D': [4, 8, 12, 16, 20], 'target': [0, 1, 1, 0, 1]})
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df, target_column):
    """
    Trains a random forest classifier on the input dataframe and plots the feature importance bar plot.

    Parameters:
    df (pd.DataFrame): The input dataframe.
    target_column (str): The name of the target column.

    Returns:
    sklearn.model.RandomForestClassifier: The trained random forest classifier.
    matplotlib.axes.Axes: The Axes object of the plotted data.
    """
    # Separate features and target
    X = df.drop(target_column, axis=1)
    y = df[target_column]

    # Initialize and train the RandomForestClassifier
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_classifier.fit(X, y)

    # Get feature importances
    feature_importances = rf_classifier.feature_importances_

    # Sort feature importances in descending order
    sorted_idx = feature_importances.argsort()[::-1]
    sorted_feature_importances = feature_importances[sorted_idx]
    sorted_feature_names = X.columns[sorted_idx]

    # Plotting
    plt.figure(figsize=(10, 6))
    sns.barplot(x=sorted_feature_importances, y=sorted_feature_names, palette='viridis')
    plt.xlabel('Feature Importance Score')
    plt.ylabel('Features')
    plt.title('Visualizing Important Features')
    plt.show()

    return rf_classifier, plt.gca()
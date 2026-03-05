from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df, target_column):
    # Train a random forest classifier on the input data
    X = df.drop(target_column, axis=1)
    y = df[target_column]
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)

    # Plot the bar plot of feature importance
    feature_importances = clf.feature_importances_
    feature_names = X.columns
    plt.bar(feature_importances, feature_names, yerr=None, align='center',
            alpha=0.5, ecolor='black', capsize=10)
    plt.xlabel('Feature Importance Score')
    plt.ylabel('Features')
    plt.title('Visualizing Important Features')
    plt.show()

    # Sort the feature importances in a descending order
    sorted_feature_importances = sorted(feature_importances, reverse=True)

    # Use the feature importances on the x-axis and the feature names on the y-axis
    plt.bar(sorted_feature_importances, feature_names, yerr=None, align='center',
            alpha=0.5, ecolor='black', capsize=10)
    plt.xlabel('Feature Importance Score')
    plt.ylabel('Features')
    plt.title('Visualizing Important Features')
    plt.show()

    return clf, plt.gca()
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': [6, 7, 8, 9, 10],
                   'C': [11, 12, 13, 14, 15],
                   'D': [16, 17, 18, 19, 20],
                   'target': [0, 1, 0, 1, 0]})
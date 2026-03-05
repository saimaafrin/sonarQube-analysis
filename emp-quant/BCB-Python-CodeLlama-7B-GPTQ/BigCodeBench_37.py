from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(df, target_column):
    # Train a random forest classifier on the input data
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(df.drop(target_column, axis=1), df[target_column])

    # Plot the bar plot of feature importance
    feature_importances = clf.feature_importances_
    feature_names = df.drop(target_column, axis=1).columns
    sorted_feature_importances = sorted(feature_importances, reverse=True)
    sorted_feature_names = sorted(feature_names, key=lambda x: feature_importances[x])

    # Plot the bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(sorted_feature_names, sorted_feature_importances)
    ax.set_xlabel('Feature Importance Score')
    ax.set_ylabel('Features')
    ax.set_title('Visualizing Important Features')

    return clf, ax
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15]})
target_column = 'A'
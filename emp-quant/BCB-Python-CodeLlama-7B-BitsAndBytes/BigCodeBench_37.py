
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df, target_column):
    # Train a random forest classifier on the input data
    X = df.drop(target_column, axis=1)
    y = df[target_column]
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)

    # Plot the feature importances
    feature_importances = clf.feature_importances_
    feature_names = X.columns
    plt.bar(feature_names, feature_importances)
    plt.xlabel('Feature Importance Score')
    plt.ylabel('Features')
    plt.title('Visualizing Important Features')
    plt.show()

    return clf
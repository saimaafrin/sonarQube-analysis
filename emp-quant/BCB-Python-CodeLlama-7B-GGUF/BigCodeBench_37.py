
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df, target_column):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df.drop(target_column, axis=1), df[target_column], test_size=0.2, random_state=42)
    
    # Train a random forest classifier on the training data
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    # Get the feature importances
    feature_importances = clf.feature_importances_
    
    # Sort the feature importances in descending order
    sorted_importances = sorted(feature_importances, reverse=True)
    
    # Plot the feature importances
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=sorted_importances, y=X_train.columns, ax=ax)
    ax.set_xlabel('Feature Importance Score')
    ax.set_ylabel('Features')
    ax.set_title('Visualizing Important Features')
    plt.show()
    
    return clf, ax
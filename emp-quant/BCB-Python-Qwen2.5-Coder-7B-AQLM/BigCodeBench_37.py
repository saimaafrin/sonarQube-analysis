
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df, target_column):
    # Separate the features and the target
    X = df.drop(target_column, axis=1)
    y = df[target_column]
    
    # Initialize the RandomForestClassifier
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Train the classifier
    rf_classifier.fit(X, y)
    
    # Get feature importances
    feature_importances = rf_classifier.feature_importances_
    
    # Sort feature importances in descending order
    sorted_idx = feature_importances.argsort()[::-1]
    sorted_importances = feature_importances[sorted_idx]
    sorted_feature_names = X.columns[sorted_idx]
    
    # Plotting the feature importance bar plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x=sorted_importances, y=sorted_feature_names)
    plt.xlabel('Feature Importance Score')
    plt.ylabel('Features')
    plt.title('Visualizing Important Features')
    plt.show()
    
    return rf_classifier, plt.gca()
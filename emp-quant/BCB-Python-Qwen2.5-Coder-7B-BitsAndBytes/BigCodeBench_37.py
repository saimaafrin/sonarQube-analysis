
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df, target_column):
    # Separate features and target
    X = df.drop(target_column, axis=1)
    y = df[target_column]
    
    # Initialize and train the Random Forest Classifier
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_classifier.fit(X, y)
    
    # Get feature importances
    feature_importances = rf_classifier.feature_importances_
    
    # Create a DataFrame for better visualization
    feature_imp_df = pd.DataFrame({
        'Feature': X.columns,
        'Importance': feature_importances
    })
    
    # Sort the features by importance in descending order
    feature_imp_df.sort_values(by='Importance', ascending=False, inplace=True)
    
    # Plotting the feature importance
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Importance', y='Feature', data=feature_imp_df)
    plt.xlabel('Feature Importance Score')
    plt.ylabel('Features')
    plt.title('Visualizing Important Features')
    plt.show()
    
    return rf_classifier, plt.gca()

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt
import os

def task_func(file_path='arena.csv', target_column='Index', seed=42):
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError("The specified file path does not exist.")
    
    # Load the data from the CSV file
    data = pd.read_csv(file_path)
    
    # Check if the target column exists in the data
    if target_column not in data.columns:
        raise ValueError(f"The target column '{target_column}' is not found in the CSV file.")
    
    # Drop rows with NaN values
    data = data.dropna()
    
    # Split the data into features and target
    X = data.drop(target_column, axis=1)
    y = data[target_column]
    
    # Initialize and train the random forest classifier
    rf_model = RandomForestClassifier(n_estimators=100, random_state=seed)
    rf_model.fit(X, y)
    
    # Get the feature importances
    importances = rf_model.feature_importances_
    
    # Plot the feature importances
    plt.figure(figsize=(10, 6))
    sns.barplot(x=X.columns, y=importances, palette="viridis")
    plt.xlabel('Features')
    plt.ylabel('Importance')
    plt.title('Feature Importances')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    return plt.gca(), importances
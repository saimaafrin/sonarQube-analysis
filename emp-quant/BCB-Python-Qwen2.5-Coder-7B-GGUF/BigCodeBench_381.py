
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt
import os

def task_func(file_path='arena.csv', target_column='Index', seed=42):
    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The specified file_path '{file_path}' does not lead to a valid file.")
    
    # Load the data
    data = pd.read_csv(file_path)
    
    # Check if the target column exists
    if target_column not in data.columns:
        raise ValueError(f"The specified target_column '{target_column}' is not found in the CSV file's columns.")
    
    # Drop rows with any NaN values
    data = data.dropna()
    
    # Check for infinity or values too large for dtype('float32')
    if data.isin([np.inf, -np.inf]).any().any() or data.max().max() > np.finfo(np.float32).max:
        raise ValueError("Input data contains NaN, infinity or a value too large for dtype('float32').")
    
    # Separate features and target variable
    X = data.drop(columns=[target_column])
    y = data[target_column]
    
    # Initialize and train the random forest model
    rf_model = RandomForestClassifier(n_estimators=100, random_state=seed)
    rf_model.fit(X, y)
    
    # Get feature importances
    importances = rf_model.feature_importances_
    
    # Plot feature importances
    plt.figure(figsize=(10, 6))
    sns.barplot(x=X.columns, y=importances)
    plt.title('Feature Importances')
    plt.xlabel('Features')
    plt.ylabel('Importance')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    return plt.gca(), importances
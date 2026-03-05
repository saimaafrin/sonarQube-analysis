import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt
import os
def task_func(file_path='arena.csv', target_column='Index', seed=42):
    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The specified file_path does not lead to a valid file: {file_path}")
    
    # Load the data
    df = pd.read_csv(file_path)
    
    # Check if the target column exists
    if target_column not in df.columns:
        raise ValueError(f"The specified target_column '{target_column}' is not found in the CSV file's columns.")
    
    # Drop rows with any NaN values
    df = df.dropna()
    
    # Check for infinity and values too large for dtype('float32')
    if df.isin([np.inf, -np.inf]).any().any():
        raise ValueError("The input data contains NaN, infinity or a value too large for dtype('float32').")
    
    # Separate features and target
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    # Initialize and train the RandomForestClassifier
    rf_model = RandomForestClassifier(n_estimators=100, random_state=seed)
    rf_model.fit(X, y)
    
    # Get feature importances
    importances = rf_model.feature_importances_
    
    # Plotting the feature importances
    plt.figure(figsize=(10, 6))
    sns.barplot(x=importances, y=X.columns, orient='h')
    plt.title('Feature Importances')
    plt.xlabel('Importance')
    plt.ylabel('Features')
    plt.show()
    
    # Return the Axes object and the importances array
    return plt.gca(), importances
file_path = 'arena.csv'
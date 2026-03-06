
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt
import os

def task_func(file_path='arena.csv', target_column='Index', seed=42):
    """
    Trains a random forest model on data from a CSV file, using one column as the target variable (y) 
    and the rest as features (X), and visualizes the feature importances in a bar plot.

    Parameters:
    - file_path (str): Path to the CSV file.
    - target_column (str): The name of the column to be used as the target variable.
    - seed (int): Seed for reproducibility.

    Returns:
    - matplotlib.axes.Axes: Axes object displaying the bar plot of feature importances.
    - numpy.ndarray: Array containing the feature importances derived from the random forest model.
    
    Raises:
    - FileNotFoundError: If the specified file_path does not lead to a valid file.
    - ValueError: If the specified target_column is not found in the CSV file's columns, or if the input data contains NaN, infinity or a value too large for dtype('float32').
    """
    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # Load the data
    df = pd.read_csv(file_path)
    
    # Check if the target column exists
    if target_column not in df.columns:
        raise ValueError(f"The target column '{target_column}' is not found in the CSV file's columns.")
    
    # Drop rows with any NaN values
    df.dropna(inplace=True)
    
    # Separate features and target
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    # Initialize and fit the Random Forest Classifier
    rf_model = RandomForestClassifier(n_estimators=100, random_state=seed)
    rf_model.fit(X, y)
    
    # Get feature importances
    importances = rf_model.feature_importances_
    
    # Plotting the feature importances
    plt.figure(figsize=(10, 6))
    sns.barplot(x=X.columns, y=importances)
    plt.title('Feature Importances')
    plt.xlabel('Features')
    plt.ylabel('Importance')
    plt.xticks(rotation=45)
    plt.show()
    
    return plt.gca(), importances
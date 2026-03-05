import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
def task_func(csv_file_path, target_column="target", test_size=0.2, n_estimators=100):
    """
    Trains a Random Forest classifier on a CSV file and generates a formatted classification report.

    Parameters:
    csv_file_path (str): The path to the CSV file.
    target_column (str): The name of the column containing the target variable.
    test_size (float): The proportion of the dataset to include in the test split.
    n_estimators (int): The number of trees in the forest.

    Returns:
    str: A formatted classification report.

    Raises:
    ValueError: If the specified target_column is not found in the CSV file.
    """
    # Load the data
    data = pd.read_csv(csv_file_path)
    
    # Check if the target_column exists in the data
    if target_column not in data.columns:
        raise ValueError(f"The specified target_column '{target_column}' is not found in the CSV file.")
    
    # Separate features and target
    X = data.drop(columns=[target_column])
    y = data[target_column]
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    
    # Initialize and train the Random Forest classifier
    clf = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    clf.fit(X_train, y_train)
    
    # Make predictions
    y_pred = clf.predict(X_test)
    
    # Generate and return the classification report
    report = classification_report(y_test, y_pred)
    return report
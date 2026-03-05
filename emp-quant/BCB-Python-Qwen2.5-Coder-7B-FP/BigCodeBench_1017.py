import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
def task_func(csv_file_path, target_column="target", test_size=0.2, n_estimators=100):
    """
    Trains a Random Forest classifier on a CSV file and generates a classification report.

    Parameters:
    - csv_file_path: str, the path to the CSV file.
    - target_column: str, the name of the column containing the target variable.
    - test_size: float, the proportion of the dataset to include in the test split.
    - n_estimators: int, the number of trees in the forest.

    Returns:
    - str: A formatted classification report.
    """
    # Load the dataset
    try:
        df = pd.read_csv(csv_file_path)
    except Exception as e:
        raise ValueError(f"Error reading the CSV file: {e}")

    # Check if the target column exists
    if target_column not in df.columns:
        raise ValueError(f"The target column '{target_column}' is not found in the CSV file.")

    # Split the dataset into features and target
    X = df.drop(target_column, axis=1)
    y = df[target_column]

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    # Initialize and train the Random Forest classifier
    rf_classifier = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    rf_classifier.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = rf_classifier.predict(X_test)

    # Generate and return the classification report
    report = classification_report(y_test, y_pred)
    return report
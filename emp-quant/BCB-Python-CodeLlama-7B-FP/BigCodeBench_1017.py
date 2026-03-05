import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
def task_func(csv_file_path, target_column="target", test_size=0.2, n_estimators=100):
    """
    Processes a CSV file to train a Random Forest classifier and generates a formatted classification report.

    Args:
        csv_file_path (str): Path to the CSV file.
        target_column (str): Name of the target column in the CSV file.
        test_size (float): Proportion of the dataset to include in the test split.
        n_estimators (int): Number of trees in the Random Forest classifier.

    Returns:
        str: A formatted classification report.

    Raises:
        ValueError: If the specified target_column is not found in the CSV file.
    """
    # Load the CSV file
    df = pd.read_csv(csv_file_path)

    # Check if the target column is present in the CSV file
    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found in CSV file.")

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(df.drop(target_column, axis=1), df[target_column], test_size=test_size)

    # Train a Random Forest classifier on the training data
    clf = RandomForestClassifier(n_estimators=n_estimators)
    clf.fit(X_train, y_train)

    # Generate a classification report for the test data
    y_pred = clf.predict(X_test)
    report = classification_report(y_test, y_pred)

    return report
csv_file_path = "data.csv"
target_column = "target"
test_size = 0.2
n_estimators = 100
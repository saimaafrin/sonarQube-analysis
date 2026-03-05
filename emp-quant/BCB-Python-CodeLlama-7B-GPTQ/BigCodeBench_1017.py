import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
def task_func(csv_file_path, target_column="target", test_size=0.2, n_estimators=100):
    """
    Processes a CSV file to train a Random Forest classifier and generates a formatted classification report.
    """
    # Check if the target column is in the CSV file
    if target_column not in pd.read_csv(csv_file_path).columns:
        raise ValueError(f"Target column '{target_column}' not found in CSV file.")

    # Load the data
    data = pd.read_csv(csv_file_path)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data.drop(target_column, axis=1), data[target_column], test_size=test_size)

    # Train a Random Forest classifier
    clf = RandomForestClassifier(n_estimators=n_estimators)
    clf.fit(X_train, y_train)

    # Generate a classification report
    y_pred = clf.predict(X_test)
    report = classification_report(y_test, y_pred)

    # Print the report
    print(report)
csv_file_path = "data.csv"
target_column = "target"
test_size = 0.2
n_estimators = 100
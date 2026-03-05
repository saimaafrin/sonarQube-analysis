
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def task_func(csv_file_path, target_column="target", test_size=0.2, n_estimators=100):
    # Load the dataset
    try:
        df = pd.read_csv(csv_file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found at {csv_file_path}")
    
    # Check if the target column exists
    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found in the CSV file.")
    
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df.drop(target_column, axis=1), df[target_column], test_size=test_size, random_state=42)
    
    # Initialize and train the Random Forest classifier
    clf = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    clf.fit(X_train, y_train)
    
    # Predict on the test set
    y_pred = clf.predict(X_test)
    
    # Generate and print the classification report
    report = classification_report(y_test, y_pred)
    print(report)
    
    # Return the classification report as a string
    return str(report)
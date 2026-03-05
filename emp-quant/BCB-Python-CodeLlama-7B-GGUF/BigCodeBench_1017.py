
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def task_func(csv_file_path, target_column="target", test_size=0.2, n_estimators=100):
    # Load the CSV file
    df = pd.read_csv(csv_file_path)
    
    # Check if the target column is present in the dataframe
    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found in CSV file")
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df.drop(target_column, axis=1), df[target_column], test_size=test_size)
    
    # Train a Random Forest classifier on the training data
    clf = RandomForestClassifier(n_estimators=n_estimators)
    clf.fit(X_train, y_train)
    
    # Evaluate the model on the testing data
    y_pred = clf.predict(X_test)
    report = classification_report(y_test, y_pred)
    
    # Print the classification report
    print(report)
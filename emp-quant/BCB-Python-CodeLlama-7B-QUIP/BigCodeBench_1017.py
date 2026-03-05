
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def task_func(csv_file_path, target_column="target", test_size=0.2, n_estimators=100):
    # Load the CSV file
    df = pd.read_csv(csv_file_path)

    # Preprocess the data
    X = df.drop(target_column, axis=1)
    y = df[target_column]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

    # Train the Random Forest classifier
    clf = RandomForestClassifier(n_estimators=n_estimators)
    clf.fit(X_train, y_train)

    # Evaluate the classifier on the testing set
    y_pred = clf.predict(X_test)
    y_true = y_test

    # Generate a classification report
    report = classification_report(y_true, y_pred)

    return report
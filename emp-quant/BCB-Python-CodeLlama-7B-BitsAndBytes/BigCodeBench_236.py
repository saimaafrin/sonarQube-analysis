
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def task_func(df, test_size=0.2, random_state=42):
    # Check if input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")

    # Drop duplicate rows with the same 'Name'
    df = df.drop_duplicates(subset=['Name'])

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df['Age'], df['Score'], test_size=test_size, random_state=random_state)

    # Train a Random Forest Classifier on the training data
    clf = RandomForestClassifier(n_estimators=100, random_state=random_state)
    clf.fit(X_train, y_train)

    # Make predictions on the testing data
    y_pred = clf.predict(X_test)

    # Evaluate the model using accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Return the accuracy as a float value
    return accuracy
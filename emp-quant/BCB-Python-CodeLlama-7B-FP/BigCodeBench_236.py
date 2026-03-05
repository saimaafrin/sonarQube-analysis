import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
def task_func(df, test_size=0.2, random_state=42):
    """
    Predicts categories based on 'Age' and 'Score' in a given DataFrame using a Random Forest Classifier.
    Rows with duplicate 'Name' entries are dropped before the prediction.
    The function uses a Random Forest Classifier from sklearn to make predictions and evaluates the model using accuracy.
    The function should raise the exception for:
        - The function will raise a ValueError is input df is not a DataFrame.
    The function should output with:
        - float: The accuracy of the prediction as a float value.
    """
    # Check if input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")

    # Drop duplicate rows
    df.drop_duplicates(subset=['Name'], inplace=True)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df[['Age', 'Score']], df['Category'], test_size=test_size, random_state=random_state)

    # Train Random Forest Classifier
    clf = RandomForestClassifier(n_estimators=100, random_state=random_state)
    clf.fit(X_train, y_train)

    # Make predictions on testing set
    y_pred = clf.predict(X_test)

    # Evaluate model using accuracy
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
                   'Age': [25, 30, 35, 25, 30, 35],
                   'Score': [85, 90, 95, 85, 90, 95],
                   'Category': ['A', 'B', 'C', 'A', 'B', 'C']})
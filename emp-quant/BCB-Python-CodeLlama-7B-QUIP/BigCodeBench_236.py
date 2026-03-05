
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def task_func(df, test_size=0.2, random_state=42):
    # Check if input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")

    # Drop duplicates
    df = df.drop_duplicates(subset=['Name'])

    # Split data into training and testing sets
    X = df.drop('Score', axis=1)
    y = df['Score']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Train the model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Make predictions on the testing set
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy
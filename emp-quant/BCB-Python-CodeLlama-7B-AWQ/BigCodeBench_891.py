import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
def task_func(csv_file_path, attribute, test_size=0.2, random_state=42):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Separate the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        df.drop(columns=attribute),
        df[attribute],
        test_size=test_size,
        random_state=random_state
    )

    # Create a linear regression model and fit the data
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    predictions = model.predict(X_test)

    # Return the trained model and the predictions
    return model, predictions
csv_file_path = "data.csv"
attribute = "target"
test_size = 0.2
random_state = 42
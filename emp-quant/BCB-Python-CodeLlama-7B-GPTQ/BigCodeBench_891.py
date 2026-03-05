import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
def task_func(csv_file_path, attribute, test_size=0.2, random_state=42):
    # Read the CSV file and create a pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Separate the data into training and testing sets
    X = df.drop(columns=attribute)
    y = df[attribute]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Train a linear regression model on the training set
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the testing set
    y_pred = model.predict(X_test)

    # Return the trained model and the predicted values
    return model, y_pred
csv_file_path = "data.csv"
attribute = "target"
test_size = 0.2
random_state = 42
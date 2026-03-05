
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def task_func(csv_file_path, attribute, test_size=0.2, random_state=42):
    # Load the data
    data = pd.read_csv(csv_file_path)

    # Separate the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data[attribute], data['target'], test_size=test_size, random_state=random_state)

    # Train the model
    model = LinearRegression().fit(X_train, y_train)

    # Make predictions on the testing set
    predictions = model.predict(X_test)

    return (model, predictions)
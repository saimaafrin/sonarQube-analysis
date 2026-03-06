
import pandas as pd
from sklearn.linear_model import LinearRegression

DATA = {
    "Area_String": ["1,000", "2,000", "3,000", "4,000", "5,000"],
    "Price": [100, 200, 300, 400, 500],
}

def task_func(area_string, data=DATA):
    # Convert the area string to a float
    area = float(area_string.replace(",", ""))

    # Create a Pandas DataFrame from the data
    df = pd.DataFrame(data)

    # Convert the Area_String column to a float
    df["Area_String"] = df["Area_String"].astype(float)

    # Split the data into training and testing sets
    X = df["Area_String"]
    y = df["Price"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a linear regression model on the training data
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make a prediction on the testing data
    y_pred = model.predict(X_test)

    # Return the predicted price for the given area
    return y_pred[0]
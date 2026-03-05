import pandas as pd
from sklearn.linear_model import LinearRegression
DATA = {
    "Area_String": ["1,000", "2,000", "3,000", "4,000", "5,000"],
    "Price": [100, 200, 300, 400, 500],
}
def task_func(area_string, data=DATA):
    """
    Predicts the price based on a given area after training a linear regression model.

    Args:
        area_string (str): The area to predict the price for.
        data (dict): The data to train the linear regression model on.

    Returns:
        float: The predicted price for the given area.
    """
    # Convert the area string to a float
    area = float(area_string.replace(",", ""))

    # Create a Pandas DataFrame from the data
    df = pd.DataFrame(data)

    # Drop the "Area_String" column since it is no longer needed
    df.drop(columns=["Area_String"], inplace=True)

    # Split the data into training and testing sets
    X = df[["Area"]]
    y = df["Price"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a linear regression model on the training data
    reg = LinearRegression()
    reg.fit(X_train, y_train)

    # Make predictions on the testing data
    predictions = reg.predict(X_test)

    # Return the predicted price for the given area
    return predictions[0]
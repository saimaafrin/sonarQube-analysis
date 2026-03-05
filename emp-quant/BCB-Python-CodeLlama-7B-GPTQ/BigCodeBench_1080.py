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

    # Split the data into features and target
    X = df["Area_String"]
    y = df["Price"]

    # Train a linear regression model on the data
    model = LinearRegression()
    model.fit(X, y)

    # Make a prediction on the given area
    prediction = model.predict([area])[0]

    return prediction
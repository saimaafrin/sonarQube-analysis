
import pandas as pd
from sklearn.linear_model import LinearRegression

DATA = {
    "Area_String": ["1,000", "2,000", "3,000", "4,000", "5,000"],
    "Price": [100, 200, 300, 400, 500],
}

def task_func(area_string, data=DATA):
    # Convert the area_string to a float
    area = float(area_string.replace(',', '.'))
    
    # Prepare the data for the model
    X = data["Area_String"].str.replace(',', '.').astype(float).values.reshape(-1, 1)
    y = data["Price"].values
    
    # Train the linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict the price for the given area
    predicted_price = model.predict([[area]])
    
    return float(predicted_price[0])

import pandas as pd
from sklearn.linear_model import LinearRegression

DATA = {
    "Area_String": ["1,000", "2,000", "3,000", "4,000", "5,000"],
    "Price": [100, 200, 300, 400, 500],
}

def task_func(area_string, data=DATA):
    # Convert the string to a numeric value
    area_numeric = int(area_string.replace(',', ''))
    
    # Prepare the data
    df = pd.DataFrame(data)
    X = df[['Area_String']].values.astype(float).reshape(-1, 1)
    y = df['Price'].values
    
    # Train the linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict the price for the given area
    predicted_price = model.predict([[area_numeric]])
    
    return float(predicted_price[0])
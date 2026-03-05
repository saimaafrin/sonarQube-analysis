import pandas as pd
from sklearn.linear_model import LinearRegression
DATA = {
    "Area_String": ["1,000", "2,000", "3,000", "4,000", "5,000"],
    "Price": [100, 200, 300, 400, 500],
}
def task_func(area_string, data=DATA):
    # Convert the area string to a float
    area = float(area_string.replace(',', '.'))
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    
    # Convert the Area_String column to float
    df['Area'] = df['Area_String'].str.replace(',', '.').astype(float)
    
    # Drop the Area_String column
    df = df.drop(columns=['Area_String'])
    
    # Split the data into features (X) and target (y)
    X = df[['Area']]
    y = df['Price']
    
    # Create a LinearRegression model
    model = LinearRegression()
    
    # Train the model
    model.fit(X, y)
    
    # Predict the price for the given area
    predicted_price = model.predict([[area]])
    
    # Return the predicted price as a float
    return float(predicted_price[0])
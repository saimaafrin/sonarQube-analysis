
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load data
data = pd.DataFrame(DATA)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(data[["Area_String"]], data["Price"])

# Define the function to predict the price based on the given area
def predict_price(area_string):
    # Convert the area to a numerical value
    area = float(area_string)

    # Predict the price using the trained model
    predicted_price = model.predict([[area]])

    # Return the predicted price
    return predicted_price
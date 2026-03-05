
import pandas as pd
from sklearn.linear_model import LinearRegression

def task_func(d, target='z'):
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(d)
    
    # Extract the target variable and the predictor variable
    X = df[['x']]
    y = df[target]
    
    # Initialize the LinearRegression model
    model = LinearRegression()
    
    # Fit the model to the data
    model.fit(X, y)
    
    # Return the model
    return model

# Create the model
model = task_func(data, target='y')

# Check if the model is an instance of LinearRegression
print(isinstance(model, LinearRegression))  # Output: True
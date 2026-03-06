
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def task_func(df1, df2, features=["feature1", "feature2", "feature3"], target="target"):
    # Merge the two dataframes on the 'id' column
    merged_df = pd.merge(df1, df2, on='id')
    
    # Select the features and target from the merged dataframe
    X = merged_df[features]
    y = merged_df[target]
    
    # Create a linear regression model
    model = LinearRegression()
    
    # Fit the model to the data
    model.fit(X, y)
    
    # Get the coefficients and intercept
    coefficients = model.coef_.tolist()
    intercept = model.intercept_
    
    # Predict the values
    predictions = model.predict(X)
    
    # Calculate the residuals
    residuals = y - predictions
    
    # Plot the residuals
    fig, ax = plt.subplots()
    ax.scatter(predictions, residuals)
    ax.set_title('Residuals Plot')
    ax.set_xlabel('Predicted Values')
    ax.set_ylabel('Residuals')
    
    # Return the results as a dictionary
    return {
        'coefficients': coefficients,
        'intercept': intercept,
        'residuals_plot': ax
    }
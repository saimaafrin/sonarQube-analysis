
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def task_func(df1, df2, features=["feature1", "feature2", "feature3"], target="target"):
    # Merge the two dataframes on the 'id' column
    merged_df = df1.merge(df2, on='id')
    
    # Initialize the LinearRegression model
    model = LinearRegression()
    
    # Fit the model with the specified features and target
    model.fit(merged_df[features], merged_df[target])
    
    # Get the coefficients and intercept
    coefficients = model.coef_
    intercept = model.intercept_
    
    # Get the predicted values and residuals
    predicted_values = model.predict(merged_df[features])
    residuals = merged_df[target] - predicted_values
    
    # Plot the residuals
    fig, ax = plt.subplots()
    ax.scatter(predicted_values, residuals, c='b', alpha=0.5)
    ax.set_title('Residuals Plot')
    ax.set_xlabel('Predicted Values')
    ax.set_ylabel('Residuals')
    
    # Return the results as a dictionary
    return {
        'coefficients': coefficients,
        'intercept': intercept,
        'residuals_plot': ax
    }
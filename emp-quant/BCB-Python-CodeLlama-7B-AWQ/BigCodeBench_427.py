import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
def task_func(df1, df2, features=["feature1", "feature2", "feature3"], target="target"):
    # Merge the two dataframes based on the 'id' column
    df = pd.merge(df1, df2, on="id")

    # Perform linear regression using the specified features to predict the target
    lm = LinearRegression()
    lm.fit(df[features], df[target])

    # Extract the regression coefficients and intercept
    coefficients = lm.coef_
    intercept = lm.intercept_

    # Plot the residuals
    residuals_plot = lm.residuals_plot(df[target], df[features])
    residuals_plot.set_title("Residuals Plot")
    residuals_plot.set_xlabel("Predicted Values")
    residuals_plot.set_ylabel("Residuals")

    # Return a dictionary containing the regression coefficients, intercept, and residuals plot
    return {"coefficients": coefficients, "intercept": intercept, "residuals_plot": residuals_plot}
df1 = pd.DataFrame({"id": [1, 2, 3, 4, 5], "feature1": [10, 20, 30, 40, 50], "feature2": [100, 200, 300, 400, 500]})
df2 = pd.DataFrame({"id": [1, 2, 3, 4, 5], "target": [1000, 2000, 3000, 4000, 5000]})
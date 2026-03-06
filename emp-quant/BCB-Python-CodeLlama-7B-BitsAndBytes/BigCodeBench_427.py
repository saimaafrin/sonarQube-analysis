
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def task_func(df1, df2, features=["feature1", "feature2", "feature3"], target="target"):
    # Merge the two dataframes based on the 'id' column
    df = pd.merge(df1, df2, on="id")

    # Perform linear regression using the specified features to predict the target
    lr = LinearRegression()
    lr.fit(df[features], df[target])

    # Extract the coefficients and intercept from the linear regression model
    coefficients = lr.coef_
    intercept = lr.intercept_

    # Plot the residuals
    fig, ax = plt.subplots()
    ax.scatter(df[features], df[target] - lr.predict(df[features]))
    ax.set_title("Residuals Plot")
    ax.set_xlabel("Predicted Values")
    ax.set_ylabel("Residuals")
    plt.show()

    # Return a dictionary containing the results
    return {"coefficients": coefficients, "intercept": intercept, "residuals_plot": ax}

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def task_func(df1, df2, features=["feature1", "feature2", "feature3"], target="target"):
    # Merge the two dataframes based on the 'id' column
    merged_df = pd.merge(df1, df2, on="id")

    # Create a linear regression object
    reg = LinearRegression()

    # Fit the model to the merged dataframe
    reg.fit(merged_df[features], merged_df[target])

    # Get the coefficients and intercept
    coefficients = reg.coef_
    intercept = reg.intercept_

    # Plot the residuals
    fig, ax = plt.subplots()
    ax.plot(merged_df[target], merged_df[target] - reg.predict(merged_df[features]))
    ax.set_xlabel("Predicted Values")
    ax.set_ylabel("Residuals")
    ax.set_title("Residuals Plot")

    # Return a dictionary containing the coefficients and intercept
    return {"coefficients": coefficients, "intercept": intercept, "residuals_plot": fig}
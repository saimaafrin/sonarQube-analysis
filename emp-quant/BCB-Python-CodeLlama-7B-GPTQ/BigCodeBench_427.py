import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
def task_func(df1, df2, features=["feature1", "feature2", "feature3"], target="target"):
    # Merge the two dataframes based on the 'id' column
    df = pd.merge(df1, df2, on="id")

    # Perform linear regression using the specified features to predict the target
    lr = LinearRegression()
    lr.fit(df[features], df[target])

    # Calculate the residuals
    residuals = lr.predict(df[features]) - df[target]

    # Plot the residuals
    fig, ax = plt.subplots()
    ax.plot(residuals, label="Residuals")
    ax.set_xlabel("Predicted Values")
    ax.set_ylabel("Residuals")
    ax.set_title("Residuals Plot")

    # Return a dictionary containing the regression coefficients, intercept, and residuals plot
    return {
        "coefficients": lr.coef_,
        "intercept": lr.intercept_,
        "residuals_plot": ax
    }
df1 = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "feature1": [10, 20, 30, 40, 50],
    "feature2": [100, 200, 300, 400, 500],
    "feature3": [1000, 2000, 3000, 4000, 5000],
    "target": [10000, 20000, 30000, 40000, 50000]
})
df2 = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "feature1": [10, 20, 30, 40, 50],
    "feature2": [100, 200, 300, 400, 500],
    "feature3": [1000, 2000, 3000, 4000, 5000],
    "target": [10000, 20000, 30000, 40000, 50000]
})
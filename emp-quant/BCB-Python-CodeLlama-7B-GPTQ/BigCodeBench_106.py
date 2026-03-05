import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
def task_func(df):
    """
    Performs linear regression on a DataFrame using 'date' (converted to ordinal) as the predictor for 'value'.
    It plots both the original and predicted values, showcasing the linear relationship.
    The function should raise the exception for:
        ValueError: If 'df' is not a valid DataFrame, lacks the required columns, or if 'date' column is not in datetime format.
    The function should output with:
        tuple: Consists of the LinearRegression model, the predictions array, and the matplotlib Axes object of the plot.
        The Axes object will have a title 'Value vs Date (Linear Regression Prediction)',
        x-axis labeled as 'Date (ordinal)', and y-axis labeled as 'Value'.
    """
    # Check if df is a valid DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a valid DataFrame")

    # Check if df has the required columns
    required_columns = ["date", "value"]
    if not all(column in df.columns for column in required_columns):
        raise ValueError("df must have columns 'date' and 'value'")

    # Check if 'date' column is in datetime format
    if not df["date"].dtype == "datetime64[ns]":
        raise ValueError("'date' column must be in datetime format")

    # Convert 'date' column to ordinal
    df["date"] = df["date"].dt.to_period("D")

    # Perform linear regression
    model = LinearRegression()
    model.fit(df[["date"]], df["value"])
    predictions = model.predict(df[["date"]])

    # Plot the original and predicted values
    fig, ax = plt.subplots()
    ax.plot(df["date"], df["value"], label="Original")
    ax.plot(df["date"], predictions, label="Predicted")
    ax.set_title("Value vs Date (Linear Regression Prediction)")
    ax.set_xlabel("Date (ordinal)")
    ax.set_ylabel("Value")
    ax.legend()

    return (model, predictions, ax)
df = pd.DataFrame({"date": ["2022-01-01", "2022-01-02", "2022-01-03", "2022-01-04"],
                   "value": [10, 20, 30, 40]})
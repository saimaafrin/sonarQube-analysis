import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
def task_func(df):
    """
    Performs linear regression on a DataFrame using 'date' (converted to ordinal) as the predictor for 'value'. It plots both the original and 
    predicted values, showcasing the linear relationship.

    Parameters:
        df (DataFrame): DataFrame containing 'group', 'date' (in datetime format), and 'value' columns.

    Returns:
        tuple: Consists of the LinearRegression model, the predictions array, and the matplotlib Axes object of the plot.
               The Axes object will have a title 'Value vs Date (Linear Regression Prediction)', 
               x-axis labeled as 'Date (ordinal)', and y-axis labeled as 'Value'.

    Raises:
        ValueError: If 'df' is not a valid DataFrame, lacks the required columns, or if 'date' column is not in datetime format.

    Requirements:
        - pandas
        - sklearn
        - matplotlib

    Example:
        >>> df = pd.DataFrame({
        ...     "group": ["A", "A", "A", "B", "B"],
        ...     "date": pd.to_datetime(["2022-01-02", "2022-01-13", "2022-02-01", "2022-02-23", "2022-03-05"]),
        ...     "value": [10, 20, 16, 31, 56],
        ... })
        >>> model, predictions, ax = task_func(df)
        >>> plt.show()  # Displays the plot with original and predicted values
    """
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a DataFrame")

    # Check if df has the required columns
    if not all(col in df.columns for col in ["group", "date", "value"]):
        raise ValueError("df must have columns 'group', 'date', and 'value'")

    # Check if 'date' column is in datetime format
    if not all(df["date"].dtype == "datetime64[ns]" for df in df):
        raise ValueError("'date' column must be in datetime format")

    # Convert 'date' column to ordinal
    df["date"] = df["date"].dt.to_period("D").astype("int")

    # Perform linear regression
    model = LinearRegression()
    model.fit(df[["date"]], df["value"])
    predictions = model.predict(df[["date"]])

    # Plot original and predicted values
    fig, ax = plt.subplots()
    ax.plot(df["date"], df["value"], label="Original")
    ax.plot(df["date"], predictions, label="Predicted")
    ax.set_title("Value vs Date (Linear Regression Prediction)")
    ax.set_xlabel("Date (ordinal)")
    ax.set_ylabel("Value")
    ax.legend()

    return model, predictions, ax
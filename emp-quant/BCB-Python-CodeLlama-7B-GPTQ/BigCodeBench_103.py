import matplotlib.pyplot as plt
import pandas as pd
def task_func(temperatures):
    """
    Calculate and plot the daytime temperatures for New York over a given period.

    Parameters
    ----------
    temperatures : pandas.DataFrame
        A DataFrame with columns 'date', 'time', and 'temperature'

    Returns
    -------
    matplotlib.axes.Axes
        The Axes object containing the temperature plot.

    Raises
    ------
    ValueError
        If the input DataFrame is not in the expected format or empty.
    """
    # Check if the input DataFrame is empty
    if temperatures.empty:
        raise ValueError("The input DataFrame is empty.")

    # Check if the input DataFrame has the expected columns
    expected_columns = ["date", "time", "temperature"]
    if not all(column in temperatures.columns for column in expected_columns):
        raise ValueError(
            f"The input DataFrame does not have the expected columns: {expected_columns}"
        )

    # Calculate the daytime temperatures
    daytime_temperatures = temperatures[
        (temperatures["time"] >= 12) & (temperatures["time"] < 18)
    ].groupby("date")["temperature"].mean()

    # Plot the daytime temperatures
    fig, ax = plt.subplots()
    ax.plot(daytime_temperatures.index, daytime_temperatures.values, "o-")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Daily Temperatures in New York")
    ax.tick_params(axis="x", labelrotation=45)
    return ax
temperatures = pd.DataFrame(
    {
        "date": ["2022-01-01", "2022-01-02", "2022-01-03", "2022-01-04"],
        "time": [10, 12, 14, 16],
        "temperature": [10, 20, 30, 40],
    }
)
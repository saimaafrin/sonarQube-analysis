import matplotlib.pyplot as plt
import pandas as pd
def task_func(temperatures):
    """
    Calculate and plot the daytime temperatures for New York over a given period.

    Parameters
    ----------
    temperatures : pandas.DataFrame
        A DataFrame containing the daily temperatures for New York.

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

    # Check if the input DataFrame has the correct format
    if not (temperatures.index.name == "Date" and temperatures.columns.name == "Temperature (°C)"):
        raise ValueError("The input DataFrame does not have the correct format.")

    # Calculate the daytime temperatures
    daytime_temperatures = temperatures.loc[temperatures.index.hour >= 12]

    # Plot the daytime temperatures
    fig, ax = plt.subplots()
    ax.plot(daytime_temperatures.index, daytime_temperatures.values, label="Daytime Temperatures")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Daily Temperatures in New York")
    ax.legend()

    return ax
temperatures = pd.DataFrame(
    {
        "Date": ["2022-01-01", "2022-01-02", "2022-01-03", "2022-01-04", "2022-01-05"],
        "Temperature (°C)": [10, 15, 20, 25, 30],
    },
    index=["Morning", "Afternoon", "Evening", "Night", "Midnight"],
)
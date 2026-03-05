import requests
import pandas as pd
import matplotlib.pyplot as plt
def task_func(api_url):
    """
    Fetches data from a specified API, processes the JSON response, converts it into a pandas DataFrame, and plots the data using matplotlib.
    If the data is empty, no plot is generated. If the API request fails, it raises an HTTPError. The function also checks if the provided API URL is a string.
    The function should raise the exception for:
        HTTPError: If the API request fails due to issues like network problems, invalid response, etc.
        TypeError: If the `api_url` is not a string.
    The function should output with:
        DataFrame: A pandas DataFrame with the parsed data from the API.
        Axes or None: A matplotlib Axes object representing the plot of the data, or None if the data is empty.
    """
    if not isinstance(api_url, str):
        raise TypeError("`api_url` must be a string")

    # Send API request and get response
    response = requests.get(api_url)

    # Check if API request failed
    if response.status_code != 200:
        raise HTTPError(f"API request failed with status code {response.status_code}")

    # Parse JSON response and convert to pandas DataFrame
    data = response.json()
    df = pd.DataFrame(data)

    # Check if data is empty
    if df.empty:
        return df, None

    # Plot data using matplotlib
    fig, ax = plt.subplots()
    ax.plot(df["x"], df["y"])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Plot of Data")
    return df, ax
api_url = "https://api.example.com/data"
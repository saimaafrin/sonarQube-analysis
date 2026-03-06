import requests
import pandas as pd
def task_func(api_url):
    """
    Fetches data from a specified API, processes the JSON response, converts it into a pandas DataFrame,
    and plots the data using matplotlib.
    If the data is empty, no plot is generated. If the API request fails, it raises an HTTPError.
    The function also checks if the provided API URL is a string.

    Parameters:
    - api_url (str): The URL of the API to fetch data from.

    Returns:
    - DataFrame: A pandas DataFrame with the parsed data from the API.
    - Axes or None: A matplotlib Axes object representing the plot of the data, or None if the data is empty.

    Raises:
    - HTTPError: If the API request fails due to issues like network problems, invalid response, etc.
    - TypeError: If the `api_url` is not a string.

    Requirements:
    - requests
    - pandas
    - matplotlib.pyplot

    Example:
    >>> df, plot = task_func("https://api.example.com/data")
    >>> df.head()
    >>> if plot:
    >>>     plot.show()
    """
    if not isinstance(api_url, str):
        raise TypeError("The `api_url` must be a string.")

    try:
        response = requests.get(api_url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise e

    if not response.text:
        return pd.DataFrame(), None

    data = response.json()
    df = pd.DataFrame(data)

    if not df.empty:
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.plot(df["x"], df["y"])
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("API Data")
        return df, ax
    else:
        return df, None
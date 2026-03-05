import requests
import pandas as pd
import matplotlib.pyplot as plt
def task_func(api_url):
    """
    Fetches data from a specified API, processes the JSON response, converts it into a pandas DataFrame, and plots the data using matplotlib.
    If the data is empty, no plot is generated. If the API request fails, it raises an HTTPError.
    The function also checks if the provided API URL is a string.
    """
    if not isinstance(api_url, str):
        raise TypeError("API URL must be a string")

    response = requests.get(api_url)
    if response.status_code != 200:
        raise HTTPError(f"API request failed with status code {response.status_code}")

    data = response.json()
    if not data:
        return pd.DataFrame(), None

    df = pd.DataFrame(data)
    fig, ax = plt.subplots()
    ax.plot(df["x"], df["y"])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("API Data Plot")
    return df, ax
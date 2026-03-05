
import requests
import pandas as pd
import matplotlib.pyplot as plt

def task_func(api_url):
    # Check if the API URL is a string
    if not isinstance(api_url, str):
        raise TypeError("API URL must be a string")

    # Fetch the data from the API
    try:
        response = requests.get(api_url)
    except requests.HTTPError:
        raise HTTPError("API request failed")

    # Parse the JSON response
    data = response.json()

    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Check if the data is empty
    if df.empty:
        return df, None

    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(df["x"], df["y"])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Plot of the data")
    return df, ax
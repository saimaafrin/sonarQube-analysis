
import requests
import pandas as pd
import matplotlib.pyplot as plt

def task_func(api_url):
    if not isinstance(api_url, str):
        raise TypeError("API URL must be a string")

    response = requests.get(api_url)
    if response.status_code != 200:
        raise HTTPError("API request failed with status code {}".format(response.status_code))

    data = response.json()
    if not data:
        return pd.DataFrame(), None

    df = pd.DataFrame(data)
    fig, ax = plt.subplots()
    ax.plot(df["x"], df["y"])
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("API Data Plot")
    return df, ax
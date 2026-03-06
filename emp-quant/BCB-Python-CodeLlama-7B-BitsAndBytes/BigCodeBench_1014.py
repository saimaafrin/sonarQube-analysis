
import requests
import pandas as pd
import matplotlib.pyplot as plt

def task_func(api_url):
    # Check if the API URL is a string
    if not isinstance(api_url, str):
        raise TypeError("API URL must be a string")

    # Fetch data from the API
    response = requests.get(api_url)

    # Check if the API request failed
    if response.status_code != 200:
        raise HTTPError("API request failed with status code {}".format(response.status_code))

    # Parse the JSON response into a pandas DataFrame
    data = response.json()
    df = pd.DataFrame(data)

    # Check if the data is empty
    if df.empty:
        return df, None

    # Create a matplotlib Axes object
    fig, ax = plt.subplots()

    # Plot the data
    ax.plot(df['x'], df['y'])

    # Return the DataFrame and Axes object
    return df, ax
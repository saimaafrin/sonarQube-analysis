
import requests
import pandas as pd
from matplotlib import pyplot as plt
from urllib.error import HTTPError

def task_func(api_url):
    # Check if the provided API URL is a string
    if not isinstance(api_url, str):
        raise TypeError("API URL must be a string")

    try:
        # Fetch data from the specified API
        response = requests.get(api_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        # Process the JSON response
        data = response.json()

        # Convert the data into a pandas DataFrame
        df = pd.DataFrame(data)

        # Plot the data using matplotlib
        if not df.empty:
            fig, ax = plt.subplots()
            ax.plot(df.index, df.values)
            plt.show()
            return df, ax
        else:
            return df, None
    except HTTPError as e:
        raise HTTPError(f"HTTP error occurred: {e}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")
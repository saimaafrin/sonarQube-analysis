import requests
import pandas as pd
import matplotlib.pyplot as plt
def task_func(api_url):
    # Check if the api_url is a string
    if not isinstance(api_url, str):
        raise TypeError("The api_url must be a string.")
    
    try:
        # Send a GET request to the API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        
        # Parse the JSON response
        data = response.json()
        
        # Convert the JSON data into a pandas DataFrame
        df = pd.DataFrame(data)
        
        # Check if the DataFrame is empty
        if df.empty:
            return df, None
        
        # Plot the data using matplotlib
        fig, ax = plt.subplots()
        ax.plot(df)
        return df, ax
    
    except requests.exceptions.HTTPError as e:
        # Raise an HTTPError if the API request fails
        raise HTTPError(f"HTTP error occurred: {e}")
    except Exception as e:
        # Handle other exceptions
        raise Exception(f"An error occurred: {e}")
api_url = "https://api.example.com/data"
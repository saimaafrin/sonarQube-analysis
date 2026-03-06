
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
        
        # Plot the data
        fig, ax = plt.subplots()
        df.plot(ax=ax)
        
        return df, ax
    
    except requests.exceptions.HTTPError as e:
        raise HTTPError(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None
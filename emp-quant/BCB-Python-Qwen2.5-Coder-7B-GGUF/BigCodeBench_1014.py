
import requests
import pandas as pd
import matplotlib.pyplot as plt

def task_func(api_url):
    if not isinstance(api_url, str):
        raise TypeError("The api_url must be a string.")
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
    except requests.exceptions.HTTPError as e:
        raise HTTPError(f"API request failed with HTTP error: {e}")
    
    data = response.json()
    if not data:
        return pd.DataFrame(), None
    
    df = pd.DataFrame(data)
    fig, ax = plt.subplots()
    df.plot(ax=ax)
    plt.show()
    
    return df, ax
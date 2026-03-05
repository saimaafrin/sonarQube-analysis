
import requests
import pandas as pd
import matplotlib.pyplot as plt

def task_func(api_url):
    if not isinstance(api_url, str):
        raise TypeError("The api_url must be a string.")
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
    except requests.exceptions.HTTPError as e:
        raise HTTPError(f"API request failed with HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"API request failed: {e}")
    
    if not data:
        return pd.DataFrame(), None
    
    df = pd.DataFrame(data)
    ax = df.plot(kind='bar', figsize=(10, 6))
    plt.title('Data from API')
    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.show()
    
    return df, ax
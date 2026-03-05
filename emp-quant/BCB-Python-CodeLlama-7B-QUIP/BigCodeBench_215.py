
import requests
import json
import pandas as pd
import seaborn as sns
# Constants
HEADERS = {
    'accept': 'application/json'
}
def task_func(url, parameters):
    # Retrieve data from the API endpoint
    response = requests.get(url, headers=HEADERS, params=parameters)
    # Check if the response is valid
    if response.status_code == 200:
        # Convert the data to a pandas DataFrame
        data = json.loads(response.text)
        df = pd.DataFrame(data)
        # Draw a heatmap
        fig, ax = sns.heatmap(df, ax=ax)
        return df, ax
    else:
        raise Exception("Invalid response from the API")
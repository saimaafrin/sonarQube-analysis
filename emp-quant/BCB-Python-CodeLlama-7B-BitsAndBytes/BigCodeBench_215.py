
import requests
import json
import pandas as pd
import seaborn as sns

# Constants
HEADERS = {
    'accept': 'application/json'
}

def task_func(url, parameters):
    # Retrieve data from API endpoint
    response = requests.get(url, headers=HEADERS, params=parameters)
    if response.status_code != 200:
        raise Exception('Invalid URL or data')
    data = response.json()

    # Convert data to pandas DataFrame
    df = pd.DataFrame(data)

    # Draw heatmap
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(df, annot=True, cmap='coolwarm')
    ax.set_title('Correlation between numerical characteristics')

    # Return DataFrame and Axes object
    return df, ax

# Display the heatmap
plt.show()

# Save the heatmap to a file
fig.savefig('heatmap.png')
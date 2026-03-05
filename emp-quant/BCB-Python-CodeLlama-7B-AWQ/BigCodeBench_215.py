import requests
import json
import pandas as pd
import seaborn as sns
HEADERS = {
    'accept': 'application/json'
}
def task_func(url, parameters):
    """Retrieve data from a specific API endpoint with the provided parameters, convert the data into a pandas dataframe, and draw a heatmap to show the correlation between numerical characteristics. The heatmap is displayed and also returned for further use or testing.
    The function should raise the exception for:
    This function will raise a general Expection if the url is invalid, empty data, invalid data, and url cannot be accessed.
    The function should output with:
        tuple: A tuple containing:
        DataFrame: The pandas DataFrame containing the data.
        Axes: The matplotlib Axes object of the heatmap.
    """
    try:
        # Retrieve data from the API endpoint
        response = requests.get(url, headers=HEADERS, params=parameters)
        # Check if the response is valid
        if response.status_code != 200:
            raise Exception(f"Invalid response with status code {response.status_code}")
        # Convert the response data into a pandas dataframe
        data = json.loads(response.content)
        df = pd.DataFrame(data)
        # Check if the dataframe is valid
        if df.empty:
            raise Exception("Empty data")
        # Draw a heatmap to show the correlation between numerical characteristics
        ax = sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
        # Display the heatmap
        plt.show()
        # Return the heatmap and the dataframe
        return (df, ax)
    except Exception as e:
        raise Exception(f"Error in task_func: {e}")
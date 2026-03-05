
import requests
import pandas as pd

def task_func(url: str) -> pd.DataFrame:
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            return df
        else:
            raise HTTPError(f"Failed to fetch data from {url}: {response.status_code}")
    except requests.RequestException as e:
        raise SystemError(f"Network error while fetching data from {url}: {e}")
    except ValueError:
        raise ValueError(f"Invalid JSON format: {data}")
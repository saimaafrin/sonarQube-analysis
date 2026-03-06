
import collections
import json
import requests

def task_func(user, API_URL = 'https://api.github.com/users/'):
    # Construct the URL to fetch the user's repositories
    url = f"{API_URL}{user}/repos"
    
    # Set up headers to mimic a web browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    # Send a GET request to the GitHub API
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        repos_data = json.loads(response.text)
        
        # Create a list to store repository names and their creation dates
        repo_list = []
        
        # Iterate over each repository in the data
        for repo in repos_data:
            # Extract the repository name and creation date
            repo_name = repo['name']
            creation_date = repo['created_at']
            
            # Append the repository name and creation date as a tuple to the list
            repo_list.append((repo_name, creation_date))
        
        # Sort the list of tuples by the creation date
        sorted_repo_list = sorted(repo_list, key=lambda x: x[1])
        
        # Extract just the repository names from the sorted list
        sorted_repo_names = [repo[0] for repo in sorted_repo_list]
        
        return sorted_repo_names
    else:
        # Return an empty list if the request failed
        return []
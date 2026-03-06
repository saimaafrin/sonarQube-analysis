
import ast
import requests
from bs4 import BeautifulSoup

def task_func(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        
        script_tags = soup.find_all('script')
        dicts_in_scripts = []
        
        for tag in script_tags:
            script_content = tag.string
            if script_content:
                try:
                    # Attempt to parse the script content as a Python expression
                    parsed_script = ast.literal_eval(script_content)
                    if isinstance(parsed_script, dict):
                        dicts_in_scripts.append(parsed_script)
                except (SyntaxError, ValueError):
                    # Ignore if not a valid Python literal
                    continue
        
        return dicts_in_scripts
    
    except requests.RequestException:
        # Return an empty list if there's an issue with the request
        return []
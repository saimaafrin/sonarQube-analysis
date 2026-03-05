import re
import json
from collections import defaultdict
import string
def task_func(json_string):
    # Initialize a default dictionary to store word counts
    word_count = defaultdict(int)
    
    try:
        # Load the JSON string into a Python dictionary
        data = json.loads(json_string)
        
        # Check if the 'text' field exists in the JSON data
        if 'text' not in data:
            return {}
        
        # Convert the text to lowercase
        text = data['text'].lower()
        
        # Remove punctuation using regex
        text = re.sub(f"[{string.punctuation}]", "", text)
        
        # Split the text into words
        words = text.split()
        
        # Count the frequency of each word
        for word in words:
            word_count[word] += 1
    
    except json.JSONDecodeError:
        # Return an empty dictionary if the JSON string is malformed
        return {}
    
    return dict(word_count)
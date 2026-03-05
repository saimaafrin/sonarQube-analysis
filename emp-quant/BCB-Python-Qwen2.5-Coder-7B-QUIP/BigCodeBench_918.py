
import pandas as pd
import re

# Function to replace acronyms in DataFrame
def task_func(data, mapping):
    # Function to replace acronyms in a single string
    def replace_acronym(text):
        for acronym, full_word in mapping.items():
            text = re.sub(r'\b' + re.escape(acronym) + r'\b', full_word, text)
        return text

    # Apply the replacement function to each string in the DataFrame
    for col in data.columns:
        if data[col].dtype == 'object':
            data[col] = data[col].apply(replace_acronym)

    return data

# Create a sample DataFrame
data = pd.DataFrame({
    'Acronym': ['ACM', 'NASA', 'NATO', 'UN', 'WHO'],
    'Description': ['Computer Science', 'Space Exploration', 'Defense', 'United Nations', 'World Health Organization']
})

# Apply the function
result = task_func(data, mapping)

# Print the result
print(result)
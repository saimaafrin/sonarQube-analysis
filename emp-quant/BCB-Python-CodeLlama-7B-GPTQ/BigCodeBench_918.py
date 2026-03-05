import pandas as pd
import re
def task_func(data, mapping):
    # Create a regular expression pattern from the mapping dictionary
    pattern = re.compile("|".join(mapping.keys()))

    # Replace all acronyms in the DataFrame with their full words
    data = data.applymap(lambda x: pattern.sub(lambda m: mapping[m.group(0)], x))

    return data
data = pd.DataFrame({"A": ["ACRONYM", "B", "C"], "B": ["D", "E", "F"], "C": ["G", "H", "I"]})
mapping = {"ACRONYM": "Acronym"}
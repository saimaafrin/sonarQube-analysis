import re
import pandas as pd
def task_func(input_string: str) -> pd.DataFrame:
    """
    Process a multi-line string by replacing tabs with spaces and converting it into a pandas DataFrame.
    Each non-empty line of the input string is transformed into a separate row in the DataFrame.
    The function specifically filters out empty lines and replaces tabs with single spaces in the remaining lines.
    Note that:
    - The function excludes lines that are empty or contain only whitespace.
    - Tabs within the lines are replaced with a single space.
    - For instance, a '\\t' character in the input string will be replaced by ' ' in the output DataFrame.
    """
    # Split the input string into a list of lines
    lines = input_string.splitlines()

    # Create a list to store the processed lines
    processed_lines = []

    # Iterate over the lines and process each one
    for line in lines:
        # Remove leading and trailing whitespace
        line = line.strip()

        # Check if the line is empty or contains only whitespace
        if not line:
            continue

        # Replace tabs with spaces
        line = line.replace('\t', ' ')

        # Add the processed line to the list
        processed_lines.append(line)

    # Create a DataFrame from the list of processed lines
    df = pd.DataFrame({'Text': processed_lines})

    return df
input_string = """
    This is a test
    with tabs and spaces

    This is another test
    with only spaces
"""
import textwrap
import re
def task_func(input_string, width):
    """
    Divide a multi-line string into separate strings and wrap each line to a certain width.
    """
    # Split the input string into a list of lines
    lines = input_string.splitlines()

    # Wrap each line to the specified width
    wrapped_lines = [textwrap.fill(line, width) for line in lines]

    # Join the wrapped lines back into a single string
    wrapped_string = "\n".join(wrapped_lines)

    return wrapped_string
input_string = "This is a very long string that needs to be wrapped to a certain width."
width = 20
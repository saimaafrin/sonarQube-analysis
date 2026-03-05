
import textwrap
import re

def task_func(input_string, width):
    # Split the input string into a list of lines
    lines = re.split(r'\r?\n', input_string)

    # Wrap each line to the specified width
    wrapped_lines = [textwrap.wrap(line, width) for line in lines]

    # Join the wrapped lines back together into a single string
    wrapped_string = ''.join(wrapped_lines)

    return wrapped_string
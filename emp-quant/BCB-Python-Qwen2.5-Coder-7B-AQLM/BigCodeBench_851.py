
import textwrap
import re

def task_func(input_string, width):
    # Split the input string into separate strings based on newlines
    lines = input_string.split('\n')
    
    # Wrap each line to the specified width
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]
    
    # Join the wrapped lines back into a single string with newlines
    wrapped_string = '\n'.join(wrapped_lines)
    
    return wrapped_string
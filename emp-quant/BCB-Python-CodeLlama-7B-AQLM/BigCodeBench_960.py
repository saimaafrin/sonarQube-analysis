import string
import random
def task_func(text, seed=None):
    """
    Generates a password that mirrors the structure of the given text by replacing alphabetic
    characters with random ascii lowercase letters, digits with random single-digit numbers,
    spaces wth either a random digit or random lowercase letter at equal probabilities, and
    leaving other characters unchanged.

    Parameters:
    - text (str): The text to be mirrored in the generated password. Must not be empty.
    - seed (int, optional): Seed for the random number generator. Defaults to None (not set).

    Returns:
    - str: The generated password.

    Raises:
    - ValueError: If the input text is empty.

    Requirements:
    - random
    - string

    Note:
    - This function does not handle high Unicode characters and focuses only on ASCII values.

    Examples:
    >>> task_func("hello world! 123", 0)
    'mbqmp3jytre!v553'
    >>> task_func("apple321#", seed=42)
    'uahev901#'
    """
    if not text:
        raise ValueError("Input text must not be empty.")

    random.seed(seed)

    password = ""
    for char in text:
        if char in string.ascii_letters:
            password += random.choice(string.ascii_lowercase)
        elif char in string.digits:
            password += random.choice(string.digits)
        elif char == " ":
            password += random.choice(string.ascii_lowercase + string.digits)
        else:
            password += char

    return password
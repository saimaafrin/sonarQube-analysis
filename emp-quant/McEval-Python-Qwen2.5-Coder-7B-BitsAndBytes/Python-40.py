def vigenere_decrypt(key: str, ciphertext: str) -> str:
    """
    Decrypts a ciphertext encrypted with the Vigenère cipher using the provided key.
    
    The Vigenère cipher is a method of encrypting alphabetic text by using a series of
    Caesar ciphers based on the letters of a keyword. This function reverses the process
    to recover the original plaintext from the ciphertext.

    Args:
        key (str): The encryption key used to encrypt the original plaintext.
                   This key should consist only of alphabetic characters.
        ciphertext (str): The encrypted text that needs to be decrypted.
                          The ciphertext should consist only of alphabetic characters.

    Returns:
        str: The decrypted plaintext corresponding to the input ciphertext.

    Examples:
        >>> vigenere_decrypt("CompleteVictory", "Yvqgpxaimmklongnzfwpvxmniytm")
        'Wherethereisawillthereisaway'

        >>> vigenere_decrypt("ABC", "DEF")
        'DCB'
    """
    # Ensure the key and ciphertext consist only of alphabetic characters
    if not key.isalpha() or not ciphertext.isalpha():
        raise ValueError("Key and ciphertext must consist only of alphabetic characters.")

    # Convert the key to uppercase and create a mapping of each letter to its position in the alphabet
    key = key.upper()
    key_length = len(key)
    key_positions = {letter: index for index, letter in enumerate(key)}

    # Initialize an empty string to store the decrypted plaintext
    plaintext = ""

    # Iterate over each character in the ciphertext
    for i, char in enumerate(ciphertext):
        # Calculate the position of the character in the alphabet
        char_position = ord(char.upper()) - ord("A")

        # Calculate the position of the corresponding character in the key
        key_char_position = key_positions[key[i % key_length]]

        # Calculate the position of the decrypted character
        decrypted_char_position = (char_position - key_char_position) % 26

        # Convert the decrypted character position back to a character
        decrypted_char = chr(decrypted_char_position + ord("A"))

        # Append the decrypted character to the plaintext
        plaintext += decrypted_char

    return plaintext
def test_vigenere_decrypt():
    # Test case 1: Example provided in the problem statement
    key1 = "CompleteVictory"
    ciphertext1 = "Yvqgpxaimmklongnzfwpvxmniytm"
    expected_plaintext1 = "Wherethereisawillthereisaway"
    assert vigenere_decrypt(key1, ciphertext1) == expected_plaintext1, "Test case 1 failed"

    # Test case 2: All uppercase characters
    key2 = "ABC"
    ciphertext2 = "DEF"
    expected_plaintext2 = "DDD"
    assert vigenere_decrypt(key2, ciphertext2) == expected_plaintext2, "Test case 2 failed"

    # Test case 3: All lowercase characters
    key3 = "xyz"
    ciphertext3 = "abc"
    expected_plaintext3 = "ddd"
    assert vigenere_decrypt(key3, ciphertext3) == expected_plaintext3, "Test case 3 failed"

    # Test case 4: Mixed case characters
    key4 = "MiXeD"
    ciphertext4 = "JpOeR"
    expected_plaintext4 = "XhRaO"
    assert vigenere_decrypt(key4, ciphertext4) == expected_plaintext4, "Test case 4 failed"

    # Test case 5: Key shorter than ciphertext
    key5 = "short"
    ciphertext5 = "PqrsPqrsPq"
    expected_plaintext5 = "XjdbWykeYx"
    assert vigenere_decrypt(key5, ciphertext5) == expected_plaintext5, "Test case 5 failed"

    print("All test cases passed!")

# Run the test function
test_vigenere_decrypt()
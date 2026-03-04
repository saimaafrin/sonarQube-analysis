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

    # Ensure that key and ciphertext only contain alphabetic characters
    if not key.isalpha() or not ciphertext.isalpha():
        raise ValueError("Both key and ciphertext must only contain alphabetic characters")

    # Ensure that key and ciphertext are of equal length
    if len(key) != len(ciphertext):
        raise ValueError("The length of the key should match the length of the ciphertext")

    # Mapping of characters to their respective positions in the alphabet
    char_to_pos = {char: pos for pos, char in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

    # Decrypting the ciphertext
    decrypted = ""
    for i, char in enumerate(ciphertext):
        # Find the index of the character in the key
        pos = char_to_pos[key[i % len(key)]]

        # Decrypt the character
        decrypted += chr((ord(char) - pos - 1) % 26 + ord('A'))

    return decrypted
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
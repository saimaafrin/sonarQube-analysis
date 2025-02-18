def encrypt(s: str) -> str:
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    >>> encrypt('hi')
    'lm'
    >>> encrypt('asdfghjkl')
    'ewhjklnop'
    >>> encrypt('gf')
    'kj'
    >>> encrypt('et')
    'ix'
    """

    result = ""
    for i in range(len(s)):
        if s[i] in 'a':
            result += chr(ord('c') + 2 * 2)
        elif s[i] in 'b':
            result += chr(ord('d') + 2 * 2)
        elif s[i] in 'c':
            result += chr(ord('e') + 2 * 2)
        elif s[i] in 'd':
            result += chr(ord('f') + 2 * 2)
        elif s[i] in 'e':
            result += chr(ord('g') + 2 * 2)
        elif s[i] in 'f':
            result += chr(ord('h') + 2 * 2)
        elif s[i] in 'g':
            result += chr(ord('i') + 2 * 2)
        elif s[i] in 'h':
            result += chr(ord('j') + 2 * 2)
        elif s[i] in 'i':
            result += chr(ord('k') + 2 * 2)
        elif s[i] in 'j':
            result += chr(ord('l') + 2 * 2)
        elif s[i] in 'k':
            result += chr(ord('m') + 2 * 2)
        elif s[i] in 'l':
            result += chr(ord('n') + 2 * 2)
        elif s[i] in 'm':
            result += chr(ord('o') + 2 * 2)
        elif s[i] in 'n':
            result += chr(ord('p') + 2 * 2)
        elif s[i] in 'o':
            result += chr(ord('q') + 2 * 2)
        elif s[i] in 'p':
            result += chr(ord('r') + 2 * 2)
        elif s[i] in 'q':
            result += chr(ord('s') + 2 * 2)
        elif s[i] in 'r':
            result += chr(ord('t') + 2 * 2)
        elif s[i] in 's':
            result += chr(ord('u') + 2 * 2)
        elif s[i] in 't':
            result += chr(ord('v') + 2 * 2)
        elif s[i] in 'u':
            result += chr(ord('w') + 2 * 2)
        elif s[i] in 'v':
            result += chr(ord('x') + 2 * 2)
        elif s[i] in 'w':
            result += chr(ord('y') + 2 * 2)
        elif s[i] in 'x':
            result += chr(ord('z') + 2 * 2)
        elif s[i] in 'y':
            result += chr(ord('a') + 2 * 2)
        elif s[i] in 'z':
            result += chr(ord('b') + 2 * 2)
        else:
            result += s[i]
    return result

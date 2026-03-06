import hashlib
import binascii
def task_func(salt, cursor):
    """
    Updates the passwords in a user table of an SQLite database by hashing them with SHA256, 
    using a provided salt. The function directly modifies the database via the given cursor.

    Parameters:
    - salt (str): The salt value to be appended to each password before hashing.
    - cursor (sqlite3.Cursor): A cursor object through which SQL commands are executed.

    Returns:
    - int: The number of users whose passwords were successfully updated.

    Requirements:
    - hashlib
    - binascii

    Raises:
    TypeError if the salt is not a string
    
    Example:
    >>> conn = sqlite3.connect('sample.db')
    >>> cursor = conn.cursor()
    >>> num_updated = task_func('mysalt', cursor)
    >>> print(num_updated)
    5
    """
    if not isinstance(salt, str):
        raise TypeError('salt must be a string')

    # Hash each password in the database
    cursor.execute('SELECT id, password FROM users')
    num_updated = 0
    for row in cursor.fetchall():
        id = row[0]
        password = row[1]
        hashed_password = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
        cursor.execute('UPDATE users SET password = ? WHERE id = ?', (hashed_password, id))
        num_updated += 1

    # Commit the changes to the database
    conn.commit()

    return num_updated

import sys
import sqlite3
# Constants
PATH_TO_APPEND = "path/to/whatever"
DATABASE = "path/to/database.db"

def task_func(path_to_append=PATH_TO_APPEND, database=DATABASE):
    # Append the path to sys.path
    sys.path.append(path_to_append)
    
    # Connect to the SQLite database
    conn = sqlite3.connect(database, isolation_level='DEFERRED')
    cursor = conn.cursor()
    
    # Create the table if it does not exist
    cursor.execute("CREATE TABLE IF NOT EXISTS paths (path TEXT UNIQUE)")
    
    # Insert the path into the database, avoiding duplicates
    try:
        cursor.execute("INSERT INTO paths (path) VALUES (?)", (path_to_append,))
    except sqlite3.IntegrityError:
        # Path already exists, do nothing
        pass
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    # Return the path that was appended to sys.path
    return path_to_append
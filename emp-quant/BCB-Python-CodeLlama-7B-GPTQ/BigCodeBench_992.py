import sys
import sqlite3
PATH_TO_APPEND = "path/to/whatever"
DATABASE = "path/to/database.db"
def task_func(path_to_append=PATH_TO_APPEND, database=DATABASE):
    # Append the path to sys.path
    sys.path.append(path_to_append)

    # Connect to the database
    conn = sqlite3.connect(database)
    c = conn.cursor()

    # Check if the table exists
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='paths'")
    if c.fetchone() is None:
        # Create the table if it doesn't exist
        c.execute("CREATE TABLE paths (path TEXT PRIMARY KEY)")

    # Check if the path is already in the table
    c.execute("SELECT path FROM paths WHERE path=?", (path_to_append,))
    if c.fetchone() is None:
        # Insert the path into the table
        c.execute("INSERT INTO paths (path) VALUES (?)", (path_to_append,))
        conn.commit()

    # Close the connection
    conn.close()

    # Return the path that was appended to sys.path and inserted into the database
    return path_to_append
import sys
import sqlite3
PATH_TO_APPEND = "path/to/whatever"
DATABASE = "path/to/database.db"
def task_func(path_to_append=PATH_TO_APPEND, database=DATABASE):
    """
    Appends a given path to sys.path and updates an SQLite database with the path, creating the table if needed and avoiding duplicates.
    """
    # Append the path to sys.path
    sys.path.append(path_to_append)

    # Connect to the database
    conn = sqlite3.connect(database)
    c = conn.cursor()

    # Create the table if it doesn't exist
    c.execute("CREATE TABLE IF NOT EXISTS paths (path TEXT PRIMARY KEY)")

    # Insert the path into the table
    c.execute("INSERT INTO paths (path) VALUES (?)", (path_to_append,))

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

    # Return the path that was appended to sys.path and inserted into the database
    return path_to_append
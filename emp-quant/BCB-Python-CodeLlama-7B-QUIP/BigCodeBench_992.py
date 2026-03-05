
import sys
import sqlite3

# Constants
PATH_TO_APPEND = "path/to/whatever"
DATABASE = "path/to/database.db"

def task_func(path_to_append=PATH_TO_APPEND, database=DATABASE):
    # Append the path to sys.path
    sys.path.append(path_to_append)

    # Create the table if it doesn't exist
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS sys_path (path TEXT PRIMARY KEY)")

    # Insert the path into the table
    c.execute("INSERT INTO sys_path (path) VALUES (?)", (path_to_append,))

    # Commit the changes
    conn.commit()

    # Return the path that was appended to sys.path and inserted into the database
    return path_to_append
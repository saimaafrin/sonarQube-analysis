
import sys
import sqlite3

# Constants
PATH_TO_APPEND = "path/to/whatever"
DATABASE = "path/to/database.db"

def task_func(path_to_append=PATH_TO_APPEND, database=DATABASE):
    # Connect to the database
    conn = sqlite3.connect(database)
    c = conn.cursor()

    # Check if the table exists
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='paths'")
    if not c.fetchone():
        # Create the table if it doesn't exist
        c.execute("CREATE TABLE paths (path TEXT PRIMARY KEY)")

    # Check if the path is already in the table
    c.execute("SELECT path FROM paths WHERE path=?", (path_to_append,))
    if not c.fetchone():
        # Insert the path into the table
        c.execute("INSERT INTO paths (path) VALUES (?)", (path_to_append,))
        conn.commit()
        print(f"Appended path {path_to_append} to sys.path and inserted into the database.")
    else:
        print(f"Path {path_to_append} is already in the database.")

    # Close the connection
    conn.close()

# Append the path to sys.path
sys.path.append(path_to_append)

# Call the function
task_func()
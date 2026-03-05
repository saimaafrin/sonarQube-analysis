import sqlite3
import random
def task_func(db_path,
          num_entries,
          users=['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'],
          countries=['USA', 'UK', 'Canada', 'Australia', 'India'],
          random_seed=None):
    """
    Generate an SQLite database to a given file path with random user data.
    The user data consists of a table named 'users' with columns:
    - id (integer): Used as Primary Key. numbering of entries starting at 0.
    - name (string): name of the user. sampled from 'users'
    - age (int): age of the user, where 20 <= age <= 60.
    - country (string): sampled from 'countries'
    The number of entries in the database is determined by num_entries.
    """
    # Create a new SQLite database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Create the 'users' table
    c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, country TEXT)")

    # Insert random data into the 'users' table
    for i in range(num_entries):
        name = random.choice(users)
        age = random.randint(20, 60)
        country = random.choice(countries)
        c.execute("INSERT INTO users (name, age, country) VALUES (?, ?, ?)", (name, age, country))

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

    # Return the file path of the generated SQLite database
    return db_path
conn = sqlite3.connect('test.db')
c = conn.cursor()
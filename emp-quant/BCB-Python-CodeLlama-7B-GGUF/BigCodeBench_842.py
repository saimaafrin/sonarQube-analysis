
import sqlite3
import random

def task_func(db_path,
          num_entries,
          users=['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'],
          countries=['USA', 'UK', 'Canada', 'Australia', 'India'],
          random_seed=None):
    # Create a new SQLite database
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Create a new table called 'users'
    c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, country TEXT)")

    # Insert random data into the table
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

# Open the SQLite database and print the contents of the 'users' table
conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute("SELECT * FROM users")
print(c.fetchall())
c.execute("PRAGMA table_info(users)")
print(c.fetchall())
conn.close()
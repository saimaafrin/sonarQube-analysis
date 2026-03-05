
import sqlite3
import random

def task_func(db_path,
          num_entries,
          users=['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'],
          countries=['USA', 'UK', 'Canada', 'Australia', 'India'],
          random_seed=None):
    if random_seed:
        random.seed(random_seed)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, country TEXT)")
    for i in range(num_entries):
        c.execute("INSERT INTO users (name, age, country) VALUES (?, ?, ?)",
                  (random.choice(users), random.randint(20, 60), random.choice(countries)))
    c.execute("SELECT * FROM users")
    return db_path
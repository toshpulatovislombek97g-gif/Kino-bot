import sqlite3

db = sqlite3.connect("movies.db", check_same_thread=False)
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
user_id INTEGER PRIMARY KEY
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
code TEXT PRIMARY KEY,
file_id TEXT
)
""")

db.commit()

def add_user(user_id):
cursor.execute(
"INSERT OR IGNORE INTO users (user_id) VALUES (?)",
(user_id,)
)
db.commit()

def get_users_count():
cursor.execute("SELECT COUNT(*) FROM users")
return cursor.fetchone()[0]

def add_movie(code, file_id):
cursor.execute(
"INSERT OR REPLACE INTO movies VALUES (?, ?)",
(code, file_id)
)
db.commit()

def get_movie(code):
cursor.execute(
"SELECT file_id FROM movies WHERE code=?",
(code,)
)
result = cursor.fetchone()
return result[0] if result else None

def delete_movie(code):
cursor.execute(
"DELETE FROM movies WHERE code=?",
(code,)
)
db.commit()

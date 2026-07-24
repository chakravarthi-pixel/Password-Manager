import sqlite3

# Connect to database
conn = sqlite3.connect("passwords.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS passwords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    website TEXT,
    username TEXT,
    password TEXT
)
""")

conn.commit()
conn.close()


# Add password
def add_password(website, username, password):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO passwords (website, username, password) VALUES (?, ?, ?)",
        (website, username, password)
    )

    conn.commit()
    conn.close()


# View all passwords
def view_passwords():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM passwords")

    rows = cursor.fetchall()

    conn.close()

    return rows
def search_password(website):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM passwords WHERE website=?",
        (website,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows
def delete_password(id):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM passwords WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()
import sqlite3

def update_password(id, website, username, password):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE passwords
        SET website = ?, username = ?, password = ?
        WHERE id = ?
    """, (website, username, password, id))

    conn.commit()
    conn.close()

    print("✅ Password updated successfully.")
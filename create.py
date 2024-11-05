import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("choco.db")

print("connected database sucessfully")
conn.execute ('''
        CREATE TABLE seasonal_flavors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flavor_name TEXT NOT NULL,
            description TEXT,
            season TEXT)''')

print("connected database sucessfully")
conn.execute('''
        CREATE TABLE IF NOT EXISTS ingredient_inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ingredient_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            unit TEXT
        )
    ''')

    # Table for Customer Suggestions and Allergy Concerns
print("connected database sucessfully")
conn.execute('''
        CREATE TABLE IF NOT EXISTS customer_suggestions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            flavor_suggestion TEXT,
            allergy_concern TEXT
        )
    ''')
conn.commit()

print("sucessfully")

conn.close()
import sqlite3

def add_campaign(name, dm_name, system):
    cursor.execute("""
    INSERT INTO campaigns (name, dm_name, system)
    VALUES (?, ?, ?)
""", (name, dm_name, system))
    
connection = sqlite3.connect("campaign_manager.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS campaigns (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        dm_name TEXT NOT NULL,
        system TEXT NOT NULL
    )
""")

add_campaign("Curse of Strahd", "Ryan", "D&D 5e")

connection.commit()

cursor.execute("SELECT name FROM sqlite_master where type='table';")
print(cursor.fetchall())



connection.commit()

cursor.execute("SELECT * FROM campaigns")

campaigns = cursor.fetchall()

print(campaigns)

connection.close()

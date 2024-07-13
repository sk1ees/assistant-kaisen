import sqlite3

conn = sqlite3.connect("assistant.db")

cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_commands(id integer primary key , name VARCHAR(100) , path VARCHAR(1000))"
cursor.execute(query)


# query = "INSERT INTO sys_commands VALUES (null,'audacity','C:\\Program Files\\Audacity\\Audacity.exe')"
# cursor.execute(query)
# conn.commit()

query = "CREATE TABLE IF NOT EXISTS web_commands(id integer primary key,name VARCHAR(100),url VARCHAR(1000))"
cursor.execute(query)

# cursor.execute("DELETE FROM sys_commands WHERE id = 1") deleted one data from the database
# conn.commit()

# query = "INSERT INTO web_commands VALUES (null,'youtube','https://www.youtube.com/')"
# cursor.execute(query)
# conn.commit()
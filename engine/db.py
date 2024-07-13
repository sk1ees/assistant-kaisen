import sqlite3

conn = sqlite3.connect("assistant.db")

cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_commands(id integer primary key , name VARCHAR(100) , path VARCHAR(1000))"
cursor.execute(query)


# query = "INSERT INTO sys_commands VALUES (null,'githubDesktop','C:\\Users\\dashi\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe')"
# cursor.execute(query)
# conn.commit()

query = "CREATE TABLE IF NOT EXISTS web_commands(id integer primary key,name VARCHAR(100),url VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO web_commands VALUES (null,'youtube','https://www.youtube.com/')"
# cursor.execute(query)
# conn.commit()
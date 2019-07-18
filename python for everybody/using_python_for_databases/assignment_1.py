import sqlite3

conn = sqlite3.connect('db1.sqlite3')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Ages')

cur.execute('''
CREATE TABLE Ages (
  name VARCHAR(128),
  age INTEGER
)
''')
cur.execute('DELETE FROM Ages')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Sarahjane", 25);')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Praise", 27)')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Riach", 23)')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Suzie", 30)')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Imani", 27)')
cur.execute('INSERT INTO Ages (name, age) VALUES ("Tate", 21)')
conn.commit

cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')
row = cur.fetchone()
print((row[0]))

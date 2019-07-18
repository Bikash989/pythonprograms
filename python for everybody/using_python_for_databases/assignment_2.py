import sqlite3

conn = sqlite3.connect('mydb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')


try:
    fname = input('Enter file name: ')
    if(len(fname) < 1): fname = 'mbox.txt'
    file_handle = open(fname)
    for line in file_handle:
        if not line.startswith('From: '): continue
        split_line = line.split()
        email = split_line[1]

        # find org from email
        org = email[email.find('@')+1:]
        cur.execute('SELECT count from Counts WHERE org = ? ', (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    conn.commit()   # commit all at once
    sql = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

    for row in cur.execute(sql):
        print(str(row[0]), row[1])


except Exception as e:
    print(e)

import sqlite3

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = "mbox.txt"
fh = open(fname)
result = dict()
for line in fh:
    if not line.startswith("From: "):
        continue
    pieces = line.split()
    email = pieces[1]
    org = email.split("@")[1]

    result[org] = int(result.get(org, 0)) + 1

for item in result:
    cur.execute('''INSERT INTO Counts (org, count)
                    VALUES (?, ?)''', (item, result[item]))

conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
import sqlite3
connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

queryDDL = """CREATE TABLE beatles (
                'fname' text,
                'lname' text,
                'nickname' text
            )"""

cursor.execute(queryDDL)

members = [
    ('John', 'Lennon', 'The Smart One'),
    ('Paul', 'McCartney', 'The Cute One'),
    ('George', 'Harrison', 'The Funny One'),
    ('Ringo', 'Starr', 'The Quiet One')
]

insert = 'INSERT INTO beatles VALUES (?, ?, ?)'

# Loop through the members list, inserting each member
for member in members:
    cursor.execute(insert, member)

query_select = 'SELECT fname, lname, nickname FROM beatles'
cursor.execute(query_select)

results = cursor.fetchall()
cursor.close()
connection.close()

print(results)
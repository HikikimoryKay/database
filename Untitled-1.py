import sqlite3 


con = sqlite3.connect('database.db')
cur = con.cursor()


# create_sql = '''
# CREATE TABLE IF NOT EXISTS class (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     surname TEXT,
#     mark INTEGER
# );
# '''

# cur.execute(create_sql)


# insert_sql = '''
# INSERT INTO class (name, surname, mark) VALUES
#     ('Павел', 'Лушников', 5),
#     ('Вова', 'Лемба', 5),
#     ('Вася', 'Пупкин',5);
# '''

# cur.execute(insert_sql)
# con.commit()
select = '''
SELECT * FROM class;
'''


data = cur.execute(select).fetchall()
for row in data:
    print(row)

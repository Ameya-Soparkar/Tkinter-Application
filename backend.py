import sqlite3

'''
CREATE TABLE
'''
def create_processing():
    conn=sqlite3.connect('material.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS processing (id INTEGER PRIMARY KEY, Name TEXT, wt REAL, weight REAL, quantity INTEGER)") 
    conn.commit()
    conn.close()


def create_plating():
    conn=sqlite3.connect('material.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS plating (id INTEGER PRIMARY KEY, Name TEXT, wt REAL, weight REAL, quantity INTEGER)") 
    conn.commit()
    conn.close()


def create_topack():
    conn=sqlite3.connect('material.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS topack (id INTEGER PRIMARY KEY, Name TEXT, wt REAL, weight REAL, quantity INTEGER)") 
    conn.commit()
    conn.close()

'''
INSERT INTO TABLES
'''

#mylist=[(1,'Material 1',0.035,0,0), (2,'Material 2',0.021,0,0), (3,'Material 3',0.013,0,0), (4,'Material 4',0.035,0,0), (5,'Material 5',0.065,0,0), (6,'Material 6',0.036,0,0), (7,'Material 7',0.05,0,0), (8,'Material 8',0.024,0,0), (9,'Material 9',0.017,0,0), (10,'Material 10',0.035,0,0), (11,'Material 11',0.006,0,0), (12,'Material 12',0.012,0,0), (13,'Material 13',0.017,0,0), (14,'Material 14',0.005,0,0), (15,'Material 15',0.0044,0,0), (16,'Material 16',0.057,0,0), (17,'Material 17',0.007,0,0), (18,'Material 18',0.24,0,0), (19,'Material 19',0.0237,0,0), (20,'Material 20',0.18,0,0), (21,'Material 21',0.095,0,0), (22,'Material 22',0.09,0,0),(23,'Material 23',0.058,0,0), (24,'Material 24',0.02,0,0), (25,'Material 25',0.087,0,0), (26,'Material 26',0.058,0,0), (27,'Material 27',0.098,0,0), (28,'Material 28',0.042,0,0), (29,'Material 29',0.021,0,0), (30,'Material 30',0.021,0,0), (31,'Material 31',0.122,0,0)]


def insert_processing():
    conn=sqlite3.connect('material.db')
    cur=conn.cursor()
    cur.executemany("INSERT INTO processing VALUES(?,?,?,?,?)", (mylist))
    conn.commit()
    conn.close()


def insert_plating():
    conn=sqlite3.connect('material.db')
    cur=conn.cursor()
    cur.executemany("INSERT INTO plating VALUES(?,?,?,?,?)", (mylist))
    conn.commit()
    conn.close()


def insert_topack():
    conn=sqlite3.connect('material.db')
    cur=conn.cursor()
    cur.executemany("INSERT INTO topack VALUES(?,?,?,?,?)", (mylist))
    conn.commit()
    conn.close()



'''
create_processing()
create_plating()
create_topack()
'''


'''
insert_processing()
insert_plating()
insert_topack()
'''




def command_exe():
    conn=sqlite3.connect('material.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM topack")
    rows=cur.fetchall()
    for row in rows:
        print(row)

command_exe()


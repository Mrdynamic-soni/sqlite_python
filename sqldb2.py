import sqlite3

#creating database named
conn = None
conn = sqlite3.connect( "file.db")
curs = conn.cursor()
print("database created successfully")

#creating table for database
# conn = None
# conn = sqlite3.connect( "file.db")
# curs = conn.cursor()
# base = "create table database(id int,sensor_name text,temperature float,humidity float)"
# curs.execute(base)
# print("table created succesfully in database")
    

if(curs.fetchone() ==0):
    #creating table for database
    conn = None
    conn = sqlite3.connect( "file.db")
    base = "create table database(id int,sensor_name text,temperature float,humidity float)"
    curs.execute(base)
    print("table created succesfully in database")
    
else: 
#inserting one  parameters in  database 
 base = "insert into database(id,sensor_name,temperature,humidity) values(1,'dht11',23.8,48) "
 curs.execute(base)
 conn.commit()
 print("data inserted succesfully in database")


#insering many data at once in database using executemany
 sensor_data=[(2,"dht11",23.7,56.2),
             (3,"dht11",24.1,55.8),
             (4,"dht11",25.6,55.1),
             (5,"dht11",24.9,54.3),
             (6,"dht11",24.5,54.6),
             (7,"dht11",34.0,55.1),
             (8,"dht11",26.4,45.2)]

 base = "insert into database values(?,?,?,?);"
 curs.executemany(base,sensor_data)
 conn.commit()
 print("large data added successfiully")


#fetch first line of data from database
 base = "select * from database"
 res = curs.execute(base)
 print(res.fetchall())

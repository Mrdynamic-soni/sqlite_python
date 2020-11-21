import sqlite3

#creating database named
def create():
 conn = None;
 conn = sqlite3.connect( "file.db")
 print("database created successfully")


#creating table for database
def table():
     conn = sqlite3.connect( "file.db")
     base = "create table database(id int,sensor_name text,temperature float,humidity float)"
     conn.execute(base)
     print("table created succesfully in database")

#inserting one  parameters in  database 
def put_value():
     conn = sqlite3.connect( "file.db")
     base = "insert into database(id,sensor_name,temperature,humidity) values(1,'dht11',23.8,48) "
     conn.execute(base)
     conn.commit()
     print("data inserted succesfully in database")


#insering many data at once in database using executemany
sensor_data=[(2,"dht11",23.7,56.2),
             (3,"dht11",24.1,55.8),
             (4,"dht11",25.6,55.1),
             (5,"dht11",24.9,54.3),
             (6,"dht11",24.5,54.6)]
def put_many():
    conn = sqlite3.connect("file.db")
    base = "insert into database values(?,?,?,?);"
    conn.executemany(base,sensor_data)
    conn.commit()
    print("large data added successfiully")

    #fetch first line of data from database
def fetchdata():
    conn = sqlite3.connect( "file.db")
    base = "select * from database"
    res = conn.execute(base)
    for row in res:
        print(row)

#executing all function
if __name__ == "__main__":
    create()
    table()
    put_value()
    fetchdata()
    put_many()
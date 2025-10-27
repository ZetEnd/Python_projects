from asyncio import selector_events
from math import radians
import numpy as np # installed with matplotlib
import matplotlib.pyplot as plt
import pymysql
from config import host, user, password, db_name


def data_processing(user_name, user_password, user_email):
    try:
        connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database= db_name,
        cursorclass= pymysql.cursors.DictCursor
        )
        print("successfully connected")
        print("#"*20)

        try:
        
            #with connection.cursor() as cursor:
            #    query = "CREATE TABLE Avengers (id int AUTO_INCREMENT," \
            #                          " name varchar(32)," \
            #                          " password varchar(32)," \
            #                          " email varchar(32), PRIMARY KEY (id));"

            #    cursor.execute(query)
            #    print("created successfully")



            with connection.cursor() as cursor:
                select_query = "SELECT name, password, email FROM Avengers"

                cursor.execute(select_query)

                rows = cursor.fetchall()
                for row in rows:
                    if (user_name in str(row) and user_password in str(row) and user_email in str(row)):
                        print("there is same avenger")
                    print(row)


                #query = "INSERT INTO Avengers (name, password, email) VALUES ('" + user_name + "', '" + user_password + "','" + user_email + "');"

                #cursor.execute(query)
                #connection.commit()
            
            with connection.cursor() as cursor:
                select_query = "SELECT name FROM Avengers"

                cursor.execute(select_query)

                rows = cursor.fetchall()
                for row in rows:
                    if (user_name in str(row)):
                        print("there is "+ user_name)
                    print(row)


   

                print("#" * 20)
                
        finally:
            connection.close()
    except Exception as ex:
        print("very bad")
        print(ex)


def main():
    x = np.arange(0, radians(1800), radians(12))
    plt.plot(x, np.cos(x), 'b')
    plt.show()

print("entering your name")
user_name = input()
user_password = input()
user_email = input()

data_processing(user_name, user_password, user_email)

#main()

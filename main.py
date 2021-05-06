import mysql.connector
from method1 import *
from method2 import *
from method3 import *
from method4 import *
from method5 import *

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rd43327893mysql",
    database="sdc",
    auth_plugin="mysql_native_password"
)

db_cursor = db_connection.cursor()

run = True

while run:

    print("This is a python programme which is used to manage a SDC database.")
    print("Methods:")
    print("1 -> add a new note;")
    print("2 -> edit a note;")
    print("3 -> delete a note")
    print("4 -> information about SDC")
    print("5 -> show a statistics")
    print("0 -> exit the programme")
    print()

    print()

    method = input("Choose a method:")

    print("You choose method", method)

    if method == "0":
        run = False

    elif method == "1":
        method_1(db_cursor, db_connection)

    elif method == "2":
        method_2(db_cursor, db_connection)

    elif method == "3":
        method_3(db_cursor, db_connection)

    elif method == "4":
        method_4(db_cursor, db_connection)

    elif method == "5":
        method_5(db_cursor, db_connection)



    elif method:
        print()
        print("A incorrect method! Please, try again")
        print()
    print()

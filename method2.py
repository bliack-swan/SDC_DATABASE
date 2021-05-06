def method_2(db_cursor, db_connection):
    try:
        print("Here you can edit a note")
        print()

        db_cursor.execute("SHOW TABLES;")

        tables = []

        for el in db_cursor:
            table = el[0]
            print(table)
            tables.append(table)

        print()
        table = input("Choose table:")

        if table in tables:
            db_cursor.execute("SELECT*FROM " + table + ";")

            for note in db_cursor:
                print(note)

            db_cursor.execute("SELECT id FROM " + table + ";")

            ides = []

            for id in db_cursor:
                id = list(id)
                id = str(id)
                id = "".join(id)
                ides.append(id)

            id = input("Choose an id of element, which you want to edit:")

            while "[" + id + "]" not in ides:
                id = input("Wrong id. Choose an id of element, which you want to edit from these: '" + ", ".join(ides) + "' :")

            print("You choosed an element with id=" + id)
            print()

            db_cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name='" + table + "';")

            columns = []

            for column in db_cursor:
                column = list(column)
                column = "".join(column)
                print(column)
                columns.append(column)

            print()

            col = input("Choose a column which you want to edit:")

            while col not in columns:
                col = input("Wrong name of column. Choose a column which you want to edit from these: '" + ", ".join(columns) + "' :")

            if col == "id":
                print("!!!You shouldn't enter pre-existing id values!!!")

            value = input("Input a new value:")

            confirm = input("Do you want to confirm changes '" + col + "=" + value + " for id=" + id + "'? (y/n)")

            while (confirm not in ('y', 'n')):
                confirm = input("Wrong input. Do you want to confirm changes '" + col + "=" + value + " for id=" + id + "'? (y/n)")

            if confirm == "y":
                db_cursor.execute("UPDATE " + table + " SET " + col + "= '" + value + "' WHERE id=" + id + ";")

                db_connection.commit()

                print("Changes commited!")

                print("New version of table:")

                db_cursor.execute("SELECT*FROM " + table + ";")

                for note in db_cursor:
                    print(note)

            elif confirm == "n":
                print("Changes was cancelled!")

        else:
            print()
            print("Wrong table!")
    except:
        print()
        print("Wrong id!")
def method_1(db_cursor, db_connection):
    try:
        print("Here you can create a new note")
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

            db_cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name='" + table + "';")


            insert_value = []
            notes = []

            for note in db_cursor:
                if note[0] == 'id':
                    continue
                value = input("Input value for " + note[0] + ":")
                insert_value.append(value)
                notes.append(note[0])

            insert_value = "', '".join(insert_value)
            notes = ", ".join(notes)

            creating = input("Do you want to insert values '" + insert_value + "'? (y/n)")

            while (creating not in ('y', 'n')):
                creating = input("Wrong input. Do you want to insert values '" + insert_value + "'? (y/n)")

            if creating == "y":
                db_cursor.execute("INSERT INTO " + table + "(" + notes + ")" + " VALUES ('" + insert_value + "');")

                db_connection.commit()

                print("Changes commited!")

                print("New version of table:")

                db_cursor.execute("SELECT*FROM " + table + ";")

                for note in db_cursor:
                    print(note)

            elif creating == "n":
                print("Creation of the new note was cancelled!")

        else:
            print()
            print("Wrong table!")

    except:
        print()
        print("Wrong id!")
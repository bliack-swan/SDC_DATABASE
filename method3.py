def method_3(db_cursor, db_connection):
    print("Here you can delete a note")
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

        id = input("Choose an id of element, which you want to delete:")

        while "[" + id + "]" not in ides:
            id = input("Wrong id. Choose an id of element, which you want to edit from these: '" + ", ".join(ides) + "' :")

        print("You choosed an element with id=" + id)

        confirm = input("Do you want to confirm delition of note with id=" + id + "? (y/n)")

        while (confirm not in ('y', 'n')):
            confirm = input("Wrong input. Do you want to confirm delition of note with id=" + id + "? (y/n)")

        if confirm == "y":
            db_cursor.execute("DELETE FROM " + table + " WHERE id=" + id + ";")

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
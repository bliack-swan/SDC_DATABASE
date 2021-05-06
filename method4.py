def method_4(db_cursor, db_connection):
    print("This is all available information")
    print("Info:")
    print("0-all tables;")
    print("1-construction materials list")
    print("2-buyers list")
    print("3-list of request")
    print("4-user request or user changes")

    info = input("Select a info:")

    while info not in ('0','1', '2', '3', '4'):
        info = input("Wrong input. Select a info again:")

    if info == '0':

        db_cursor.execute("SHOW TABLES;")
        print('All tables:')
        for note in db_cursor:
            print(note)

    elif info == "1":

        db_cursor.execute("SELECT*FROM construction_materials;")
        print('(id_product, supplier, count_enrolled, count_sold, country_manufacture, price)')
        for note in db_cursor:
            print(note)

    elif info == "2":

        db_cursor.execute("SELECT b.surname, b.name, b.patronymic, b.id_passport, b.series_passport, "
                          "b.telephon_number, c.city, b.street, b.house, b.flat "
                          " FROM buyers AS b JOIN city AS c ON b.city_residence = c.id_city;")
        print('(surname, name, patronymic, id_passport, series_passport, telephon_number, city_residence, '
              'street, house, flat)')
        for note in db_cursor:
            print(note)

    elif info == "3":

        db_cursor.execute("SELECT*FROM request;")

        for note in db_cursor:
            print(note)

    elif info == "4":
        try:
            request = input("Please input a right request/changes for MySQL syntax: ")

            confirm = input("Do you want to confirm your request/changes: '" + request + "'? (y/n)")

            while (confirm not in ('y', 'n')):
                confirm = input("Wrong input. Do you want to confirm your request/changes: '" + request + "'? (y/n)")

            if confirm == "y":
                db_cursor.execute(request)

                for note in db_cursor:
                    print(note)

                db_connection.commit()

            elif confirm == "n":
                print("Requst/Changes was cancelled")

        except:
            print()
            print("Wrong request!")
def method_5(db_cursor, db_connection):
    print("Here you can see some statistics")
    print("1-the most popular con_mut")
    print("2-amount of pairs of your subgroup in the day")

    statistics = input("Choose a statistics(1, 2):")

    while statistics not in ('1', '2'):
        statistics = input("Wrong number of statistics. Choose another(1 or 2):")

    if statistics == '1':


        db_cursor.execute("select construction_materials_id_product, count(1) cnt from request "
                          "where construction_materials_id_product ="
                          "(select construction_materials_id_product from request  group by "
                          "construction_materials_id_product order by count(1) desc limit 1)"
                          " order by cnt desc limit 1;")
        print()

        for note in db_cursor:
            print(note)

    if statistics == '2':
        for note in db_cursor:
            print(note)
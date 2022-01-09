first_receipt = f"""№ квитанции: "867"
Дата принятия в ремонт: 2022-01-03
Дата выдачи после ремонта: 2022-01-05
Статус: "Выдана пользователю"
Техническая информация/информация о поломке: 
Ноутбук - model='Asus', year_of_release=2019, operation_system='Windows', type_of_breakdown='не включается'"""

second_receipt = f"""№ квитанции: "735"
Дата принятия в ремонт: 2021-12-08
Дата выдачи после ремонта: 2021-12-11
Статус: "Выдана пользователю"
Техническая информация/информация о поломке: 
Ноутбук - model='Asus', year_of_release=2019, operation_system='Windows', type_of_breakdown='не работает камера'"""

third_receipt = f"""№ квитанции: "744"
Дата принятия в ремонт: 2020-01-09
Дата выдачи после ремонта: 2020-01-13
Статус: "Выдана пользователю"
Техническая информация/информация о поломке: 
Телефон - model='Xiaomi',operation_system='Android',type_of_breakdown='не работает динамик'"""

fourth_receipt = f"""№ квитанции: "540"
Дата принятия в ремонт: 2019-11-09
Дата выдачи после ремонта: 2019-11-13
Статус: "Выдана пользователю"
Техническая информация/информация о поломке: 
Телефон - model='Xiaomi', operation_system='Android', type_of_breakdown='разбит экран'"""

fifth_receipt = f"""№ квитанции: "235"
Дата принятия в ремонт: 2017-09-09
Дата выдачи после ремонта: 2017-09-13
Статус: "Выдана пользователю"
Техническая информация/информация о поломке: 
Телевизор - model='Samsung', diagonal=43, type_of_breakdown='не включается'"""

six_receipt = f"""№ квитанции: "935"
Дата принятия в ремонт: 2022-01-09
Дата выдачи после ремонта: 2022-01-13
Статус: "Выдана пользователю"
Техническая информация/информация о поломке: 
Телевизор - model='Samsung', diagonal=43, type_of_breakdown='Искажения изображения'"""


def using_a_receipt(number_of_receipt):
    if number_of_receipt == "867":
        print(first_receipt)
    elif number_of_receipt == "735":
        print(second_receipt)
    elif number_of_receipt == "744":
        print(third_receipt)
    elif number_of_receipt == "540":
        print(fourth_receipt)
    elif number_of_receipt == "235":
        print(fifth_receipt)
    elif number_of_receipt == "935":
        print(six_receipt)
    else:
        print("""Такой квитанции не существует, либо Вы ввели не корректные данные. Попробуйте ещё раз""")
        number_of_receipt = input()
        using_a_receipt(number_of_receipt)


def using_all_receipts(user_data):
    print(f"""Пользователь {user_data.surname} {user_data.name} {user_data.father_name}
Информация о обращениях в наш сервис:
    
{fifth_receipt}

{second_receipt}

{third_receipt}

{fourth_receipt}

{fifth_receipt}

{six_receipt}
""")

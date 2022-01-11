import main


user_data_petrov = main.Receipt("Петр", "Петрович", "Петров ", "Ноутбук")
equipment_data_petrov = main.Laptop("Asus", "Windows", 2019, "не включается", "2021-12-08", "2021-12-11",
                                    "Выдана пользователю", 787)

petrov_equipment_data_information = f"""№ квитанции: {equipment_data_petrov.number_of_receipt}
Пользователь(Ф.И.О): {user_data_petrov.surname} {user_data_petrov.name} {user_data_petrov.father_name}
Дата принятия в ремонт: {equipment_data_petrov.date_of_receipt}
Дата выдачи после ремонта: {equipment_data_petrov.deadline}
Статус: {equipment_data_petrov.status}
Техническая информация/информация о поломке: 
{user_data_petrov.equipment = } - {equipment_data_petrov.model = }, {equipment_data_petrov.year_of_release = }, 
{equipment_data_petrov.operation_system = }, {equipment_data_petrov.type_of_breakdown = }"""

user_data_petrov.equipment = "Телефон"
second_equipment_data_petrov = main.Phone("Samsung", "Android", "не включается", "2020-09-09", "2020-09-12",
                                          "Выдана пользователю", 252)

second_petrov_equipment_data_information = f"""№ квитанции: {second_equipment_data_petrov.number_of_receipt}
Пользователь(Ф.И.О): {user_data_petrov.surname} {user_data_petrov.name} {user_data_petrov.father_name}
Дата принятия в ремонт: {second_equipment_data_petrov.date_of_receipt}
Дата выдачи после ремонта: {second_equipment_data_petrov.deadline}
Статус: {second_equipment_data_petrov.status}
Техническая информация/информация о поломке: 
{user_data_petrov.equipment = } - {second_equipment_data_petrov.model = }, 
{second_equipment_data_petrov.operation_system = }, {second_equipment_data_petrov.type_of_breakdown = }"""

user_data_ivanov = main.Receipt("Иванов", "Иван", "Иванович ", "Телевизор")
equipment_data_ivanov = main.TV("Samsung", "42", "нет изображения", "2020-10-05", "2020-10-08",
                                "Выдана пользователю", "505")

ivanov_equipment_data_information = f"""№ квитанции: {equipment_data_ivanov.number_of_receipt}
Пользователь(Ф.И.О): {user_data_ivanov.surname} {user_data_ivanov.name} {user_data_ivanov.father_name}
.Дата принятия в ремонт: {equipment_data_ivanov.date_of_receipt}
Дата выдачи после ремонта: {equipment_data_ivanov.deadline}
Статус: {equipment_data_ivanov.status}
Техническая информация/информация о поломке: 
{user_data_ivanov.equipment = } - {equipment_data_ivanov.model = }, {equipment_data_ivanov.diagonal = }, 
{equipment_data_ivanov.type_of_breakdown = }"""

user_data_ivanov.equipment = "Телевизор"
second_equipment_data_ivanov = main.TV("Samsung", "42", "не включается", "2020-10-05", "2020-10-08",
                                       "Выдана пользователю", "752")
second_ivanov_equipment_data_information = f"""№ квитанции: {second_equipment_data_ivanov.number_of_receipt}
Пользователь(Ф.И.О): {user_data_ivanov.surname} {user_data_ivanov.name} {user_data_ivanov.father_name}
Дата принятия в ремонт: {second_equipment_data_ivanov.date_of_receipt}
Дата выдачи после ремонта: {second_equipment_data_ivanov.deadline}
Статус: {second_equipment_data_ivanov.status}
Техническая информация/информация о поломке: 
{user_data_ivanov.equipment = } - {second_equipment_data_ivanov.model = }, {second_equipment_data_ivanov.diagonal = }, 
{second_equipment_data_ivanov.type_of_breakdown = }"""

user_data_sergeev = main.Receipt("Сергей", "Сергеевич", "Сергеев ", "Телефон")
equipment_data_sergeev = main.Phone("Samsung", "Android", "не включается", "2020-09-09", "2020-09-12",
                                    "Выдана пользователю", "252")
sergeev_equipment_data_information = f"""№ квитанции: {equipment_data_sergeev.number_of_receipt}
Пользователь(Ф.И.О): {user_data_sergeev.surname} {user_data_sergeev.name} {user_data_sergeev.father_name}
Дата принятия в ремонт: {equipment_data_sergeev.date_of_receipt}
Дата выдачи после ремонта: {equipment_data_sergeev.deadline}
Статус: {equipment_data_sergeev.status}
Техническая информация/информация о поломке: 
{user_data_sergeev.equipment = } - {equipment_data_sergeev.model = }, {equipment_data_sergeev.operation_system = }, 
{equipment_data_sergeev.type_of_breakdown = }"""

petrov_data = f"{user_data_petrov.surname}{user_data_petrov.name} {user_data_petrov.father_name}"
petrov_receipts_information = f"""Информация по всем обращениям - 
{petrov_equipment_data_information}, 
{second_petrov_equipment_data_information}"""
ivanov_data = f"{user_data_ivanov.surname}{user_data_ivanov.name} {user_data_ivanov.father_name}"
ivanov_data_information = f"""Информация по всем обращениям - 
{ivanov_equipment_data_information}, 
{second_ivanov_equipment_data_information}"""
sergeev_data = f"{user_data_sergeev.surname}{user_data_sergeev.name} {user_data_sergeev.father_name}"
sergeev_data_information = f"""Информация по всем обращениям - 
{sergeev_equipment_data_information}"""

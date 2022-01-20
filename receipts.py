import models


user_data_petrov = models.Receipt("Петров", "Петр", "Петрович ", "Ноутбук", "110", "2020-09-09", "2020-09-12",
                                  "Техника выдана пользователю после ремонта")
user_data_petrov.equipment = models.Laptop("Asus", "Windows", "2019", "не включается")

first_receipt_petrov = user_data_petrov  # Квитанция

user_data_petrov = models.Receipt("Петров", "Петр", "Петрович ", "Телефон", "225", "2021-08-09", "2021-08-12",
                                  "Техника выдана пользователю после ремонта")
user_data_petrov.equipment = models.Phone("Samsung", "Android", "не включается")

second_receipt_petrov = user_data_petrov  # Квитанция

user_data_ivanov = models.Receipt("Иванов", "Иван", "Иванович ", "Телевизор", "315", "2019-09-12",
                                  "2019-09-15", "Техника выдана пользователю после ремонта")
user_data_ivanov.equipment = models.TV("Samsung", "42", "нет изображения")

first_receipt_ivanov = user_data_ivanov  # Квитанция

user_data_ivanov = models.Receipt("Иванов", "Иван", "Иванович ", "Телевизор", "554", "2020-08-12",
                                  "2020-08-15", "Техника выдана пользователю после ремонта")
user_data_ivanov.equipment = models.TV("Samsung", "42", "не включается")

second_receipt_ivanov = user_data_ivanov  # Квитанция

user_data_sergeev = models.Receipt("Сергеев", "Сергей", "Сергеевич ", "Телефон", "349", "2021-12-12",
                                   "2021-12-15", "Техника выдана пользователю после ремонта")
user_data_sergeev.equipment = models.Phone("Samsung", "Android", "не включается")

first_receipt_sergeev = user_data_sergeev  # Квитанция

petrov_data = f"{user_data_petrov.surname} {user_data_petrov.name} {user_data_petrov.father_name}"
ivanov_data = f"{user_data_ivanov.surname} {user_data_ivanov.name} {user_data_ivanov.father_name}"
sergeev_data = f"{user_data_sergeev.surname} {user_data_sergeev.name} {user_data_sergeev.father_name}"
dict_with_receipts = {petrov_data: [first_receipt_petrov, second_receipt_petrov], ivanov_data: [first_receipt_ivanov,
                      second_receipt_ivanov], sergeev_data: first_receipt_sergeev, "110": first_receipt_petrov,
                      "225": second_receipt_petrov, "315": first_receipt_ivanov, "554": second_receipt_ivanov, "349":
                      first_receipt_sergeev}


def give_out_information(choice):
    for k, v in dict_with_receipts.items():
        if k == choice:
            if isinstance(v, list):
                for i in v:
                    print(i)
            else:
                print(v)
            break
    else:
        print("Информация отсутствует, либо Вы ввели не корректные данные!")

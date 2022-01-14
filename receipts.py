import main
import moduls


current_status = main.Status("Техника выдана пользователю после ремонта")
current_date_petrov = main.Dates("2020-09-09", "2020-09-12")
user_data_petrov = main.Receipt("Петр", "Петрович", "Петров ", "Ноутбук", "110")
equipment_data_petrov = moduls.Laptop("Asus", "Windows", "2019", "не включается")
# Квитанция
first_receipt_petrov = f"""{user_data_petrov.fill_user_data()}
{equipment_data_petrov.fill_in_receipt()}
{current_date_petrov.__str__()}
{current_status.__str__()}"""

user_data_petrov.equipment = "Телефон"
user_data_petrov.number_of_receipt = "225"
second_equipment_data_petrov = moduls.Phone("Samsung", "Android", "не включается")
second_current_date_petrov = main.Dates("2021-08-09", "2021-08-12")
# Квитанция
second_receipt_petrov = f"""{user_data_petrov.fill_user_data()}
{second_equipment_data_petrov.fill_in_receipt()}
{second_current_date_petrov.__str__()}
{current_status.__str__()}"""

user_data_ivanov = main.Receipt("Иван", "Иванович", "Иванов ", "Телевизор", "315")
equipment_data_ivanov = moduls.TV("Samsung", "42", "нет изображения")
current_date_ivanov = main.Dates("2019-09-12", "2019-09-15")
# Квитанция
first_receipt_ivanov = f"""{user_data_ivanov.fill_user_data()}
{equipment_data_ivanov.fill_in_receipt()}
{current_date_ivanov.__str__()}
{current_status.__str__()}"""

user_data_ivanov.equipment = "Телевизор"
user_data_ivanov.number_of_receipt = "554"
second_equipment_data_ivanov = moduls.TV("Samsung", "42", "не включается")
second_current_date_ivanov = main.Dates("2020-08-09", "2020-08-12")
# Квитанция
second_receipt_ivanov = f"""{user_data_ivanov.fill_user_data()}
{second_equipment_data_ivanov.fill_in_receipt()}
{current_date_ivanov.__str__()}
{current_status.__str__()}"""

user_data_sergeev = main.Receipt("Сергей", "Сергеевич", "Сергеев ", "Телефон", "349")
equipment_data_sergeev = moduls.Phone("Samsung", "Android", "не включается")
current_date_sergeev = main.Dates("2021-12-12", "2021-12-15")
# Квитанция
first_receipt_sergeev = f"""{user_data_sergeev.fill_user_data()}
{equipment_data_sergeev.fill_in_receipt()}
{current_date_ivanov.__str__()}
{current_status.__str__()}"""

petrov_data = f"{user_data_petrov.surname}{user_data_petrov.name} {user_data_petrov.father_name}"
ivanov_data = f"{user_data_ivanov.surname}{user_data_ivanov.name} {user_data_ivanov.father_name}"
sergeev_data = f"{user_data_sergeev.surname}{user_data_sergeev.name} {user_data_sergeev.father_name}"
dict_with_receipts = {petrov_data: [first_receipt_petrov, second_receipt_petrov], ivanov_data: [first_receipt_ivanov,
                      second_receipt_ivanov], sergeev_data: first_receipt_sergeev, "110": first_receipt_petrov,
                      "225": second_receipt_petrov, "315": first_receipt_ivanov, "554": second_receipt_ivanov, "349":
                      first_receipt_sergeev}
number_of_receipt_dict = {"110": first_receipt_petrov, "225": second_receipt_petrov, "315": first_receipt_ivanov,
                          "554": second_receipt_ivanov, "349": first_receipt_sergeev}


def give_out_information(choice):
    for k, v in dict_with_receipts.items():
        if k == choice:
            print(v)


cur = input()
give_out_information(cur)

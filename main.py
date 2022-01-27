import models
import datetime
import random
import receipts
import admins_data
import text_information_variables


def fill_out_a_receipt(type_of_technic):
    while True:
        if type_of_technic == "Телефон":
            equipment = models.Phone(input(text_information_variables.models_text),
                                     input(text_information_variables.operation_system_text),
                                     input(text_information_variables.type_of_breakdown_text))
            break
        elif type_of_technic == "Ноутбук":
            try:
                equipment = models.Laptop(input(text_information_variables.models_text),
                                          input(text_information_variables.operation_system_text),
                                          int(input(text_information_variables.year_of_release_text)),
                                          input(text_information_variables.type_of_breakdown_text))
            except ValueError:
                print(text_information_variables.error_text)
            else:
                break
        elif type_of_technic == "Телевизор":
            try:
                equipment = models.TV(input(text_information_variables.models_text),
                                      int(input(text_information_variables.diagonal_text)),
                                      input(text_information_variables.type_of_breakdown_text))
            except ValueError:
                print(text_information_variables.error_text)
            else:
                break
        else:
            print(text_information_variables.error_text)
            type_of_technic = input(text_information_variables.type_of_technic_text)
    print(text_information_variables.personal_data_text)
    user_data = models.Receipt(input(text_information_variables.name_text),
                               input(text_information_variables.father_name_text),
                               input(text_information_variables.surname_text), equipment, random.randint(1, 1000),
                               datetime.date.today(),
                               datetime.date.today() + datetime.timedelta(random.choice(range(1, 5))),
                               "Техника сдана в ремонт")
    personal_data = f"{user_data.surname} {user_data.name} {user_data.father_name}"
    receipts.dict_with_receipts[user_data.number_of_receipt] = user_data
    if personal_data in receipts.dict_with_receipts:
        receipts.dict_with_receipts[personal_data].append(user_data)
    else:
        receipts.dict_with_receipts[personal_data] = user_data
    return user_data


def search_receipt(user_choice):
    while True:
        if user_choice == "0":
            break
        else:
            receipts.give_out_information(user_choice)
            break


def accept_a_choice(user_choice):
    if user_choice == "Сдаю в ремонт":
        print(text_information_variables.type_of_technic_text)
        current_technic = input(text_information_variables.enter_text)
        print(fill_out_a_receipt(current_technic))
    elif user_choice == "Информация":
        print(text_information_variables.welcome_information_console_text)
        current_user_choice = input(text_information_variables.enter_text)
        search_receipt(current_user_choice)
    elif user_choice == "0":
        print(text_information_variables.farewell_text)
        exit()
    elif user_choice == "Админ":
        current_login = input(text_information_variables.enter_login_text)
        current_password = input(text_information_variables.enter_password_text)
        admins_data.log_in_admin(current_login, current_password)
    else:
        print(text_information_variables.error_text)
        user_choice = input(text_information_variables.enter_data_text)
        accept_a_choice(user_choice)


def main():
    print(text_information_variables.welcome_text)
    current_choice = input(text_information_variables.enter_data_text)
    accept_a_choice(current_choice)


if __name__ == "__main__":
    while True:
        main()

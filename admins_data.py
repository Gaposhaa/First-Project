import main
import receipts
import text_information_variables


class Admins:
    def __init__(self, surname, name, father_name, login, password):
        self.surname = surname
        self.name = name
        self.father_name = father_name
        self.login = login
        self.password = password

    def __str__(self):
        return f"{self.surname} {self.name} {self.father_name}"


admin_haponenka = Admins("Гапоненко", "Артем", "Сергеевич", "Artem", "MilMir21")
admin_ivanov = Admins("Иванов", "Иван", "Иванович", "Ivan", "Iv2000")
admin_petrov = Admins("Петров", "Петр", "Петрович", "Petr", "pet2001")
admins_list_data = [admin_haponenka, admin_ivanov, admin_petrov]
admins_logins_passwords_dict = {admin_haponenka.login: admin_haponenka.password,
                                admin_ivanov.login: admin_ivanov.password, admin_petrov.login: admin_petrov.password}


def act_as_an_admin(user_choice):
    if user_choice == "1":
        for i in admins_list_data:
            print(i)
    elif user_choice == "2":
        print(text_information_variables.admin_delete_text)
        admin_choice = input(text_information_variables.enter_login_text)
        for i in admins_list_data:
            if i.login == admin_choice:
                admins_list_data.remove(i)
                for k in admins_logins_passwords_dict.keys():
                    if k == i.login:
                        admins_logins_passwords_dict.pop(k)
                    break
                else:
                    print(text_information_variables.error_text)
    elif user_choice == "3":
        print(text_information_variables.admin_add_text)
        new_admin = Admins(input(text_information_variables.surname_text), input(text_information_variables.name_text),
                           input(text_information_variables.father_name_text),
                           input(text_information_variables.enter_login_text),
                           input(text_information_variables.enter_password_text))
        admins_list_data.append(new_admin)
        admins_logins_passwords_dict[new_admin.login] = new_admin.password
    elif user_choice == "4":
        print(text_information_variables.enter_data_of_receipt_text)
        current_receipt_data = input(text_information_variables.enter_text)
        change_receipts(current_receipt_data)
    elif user_choice == "0":
        exit(main.main())
    else:
        print(text_information_variables.error_text)


def log_in_admin(login, password):
    for k, v in admins_logins_passwords_dict.items():
        if k == login and v == password:
            print(text_information_variables.welcome_admin_console_text)
            current_choice = input(text_information_variables.enter_text)
            act_as_an_admin(current_choice)
            break
    else:
        print(text_information_variables.error_text)


def change_receipts(receipt_data):
    for key, value in receipts.dict_with_receipts.items():
        if key == receipt_data:
            if isinstance(value, list):
                for i in value:
                    print(i)
                print(text_information_variables.number_of_receipts_text)
                receipt_number = input(text_information_variables.enter_text)
                change_receipts(receipt_number)
                break
            else:
                value.status = input(text_information_variables.new_status_text)
                value.date_of_receipt = input(text_information_variables.new_date_of_receipt_text)
                value.deadline = input(text_information_variables.new_deadline_text)
                receipts.dict_with_receipts[key] = value
                print(value)
            break
    else:
        print(text_information_variables.error_text)

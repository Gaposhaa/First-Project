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
admins_list_data = [str(admin_haponenka), str(admin_ivanov), str(admin_petrov)]
admins_logins_passwords_dict = {admin_haponenka.login: admin_haponenka.password,
                                admin_ivanov.login: admin_ivanov.password, admin_petrov.login: admin_petrov.password}


def act_as_an_admin(user_choice):
    if user_choice == "1":
        print(admins_list_data)
    elif user_choice == "2":
        print("Выберите админа, которого хотите удалить")
        admin_choice = input("Введите Ф.И.О. админа - ")
        for i in admins_list_data:
            if i == admin_choice:
                admins_list_data.remove(i)
                if i == str(admin_haponenka):
                    admins_logins_passwords_dict.pop(admin_haponenka.login)
                    print("Админ удален")
                    break
                elif i == str(admin_ivanov):
                    admins_logins_passwords_dict.pop(admin_ivanov.login)
                    print("Админ удален")
                    break
                elif i == str(admin_petrov):
                    admins_logins_passwords_dict.pop(admin_petrov.login)
                    print("Админ удален")
                    break
        else:
            print(text_information_variables.error_text)
    elif user_choice == "3":
        print("Введите данные админа, которого хотите добавить")
        new_admin = Admins(input("Фамилия - "), input("Имя - "), input("Очество - "), input("Логин - "),
                           input("Пароль - "))
        admins_list_data.append(str(new_admin))
        admins_logins_passwords_dict[new_admin.login] = new_admin.password
        print("Админ добавлен")
    elif user_choice == "4":
        print("Введите данные квитанции(Номер/Ф.И.О.) - ")
        current_receipt_data = input("Данные квитанции - ")
        change_receipts(current_receipt_data)
    elif user_choice == "0":
        exit(main.main())
    else:
        print(text_information_variables.error_text)


def log_in_admin(login, password):
    for k, v in admins_logins_passwords_dict.items():
        if k == login and v == password:
            print(text_information_variables.welcome_admin_console_text)
            current_choice = input("Ваш выбор - ")
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
                print("Выберите нужный номер квитанции")
                receipt_number = input("Номер квитанции - ")
                change_receipts(receipt_number)
                break
            else:
                value.status = input("Новый статус - ")
                value.date_of_receipt = input("Новая дата приема - ")
                value.deadline = input("Новая дата выдачи - ")
                receipts.dict_with_receipts[key] = value
                print(value)
            break
    else:
        print(text_information_variables.error_text)

import main


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


def accept_a_choice(user_choice):
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
                    break
                elif i == str(admin_ivanov):
                    admins_logins_passwords_dict.pop(admin_ivanov.login)
                    break
                elif i == str(admin_petrov):
                    admins_logins_passwords_dict.pop(admin_petrov.login)
                    break
    elif user_choice == "3":
        print("Введите данные аддмина, которого хотите добаваить")
        new_admin = Admins(input("Фамилия - "), input("Имя - "), input("Очество - "), input("Логин - "),
                           input("Пароль - "))
        admins_list_data.append(new_admin)
        admins_logins_passwords_dict[new_admin.login] = new_admin.password
        print("Админ добавлен")
    elif user_choice == "0":
        exit(main.main())
    else:
        print("Введены не корректные данные")


def log_in_admin(login, password):
    for k, v in admins_logins_passwords_dict.items():
        if k == login and v == password:
            print("Добро пожаловать в админ панель.\nОтобразить спсиок админов, введите - 1\n"
                  "Удалить админа, введите - 2\nДобавить админа, введите- 3\nВернуться в главное меню - 0 ")
            current_choice = input("Ваш выбор - ")
            accept_a_choice(current_choice)
            break
    else:
        print("Не корректные данные!")

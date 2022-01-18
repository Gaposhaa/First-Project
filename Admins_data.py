import main


class Admins:
    def __init__(self, surname, name, father_name, login, password):
        self.surname = surname
        self.name = name
        self.father_name = father_name
        self.login = login
        self.password = password

    def __str__(self):
        return f"Администратор: {self.surname} {self.name} {self.father_name}\nЛогин: {self.login}\n" \
               f"Пароль: {self.password}"


admin_haponenka = Admins("Гапоненко", "Артем", "Сергеевич", "Artem", "MilMir21")
haponenka_data = admin_haponenka

admin_ivanov = Admins("Иванов", "Иван", "Иванович", "Ivan", "Iv2000")
ivanov_data = admin_ivanov

admin_petrov = Admins("Петров", "Петр", "Петрович", "Petr", "pet2001")
petrov_data = admin_petrov

admins_list = [admin_haponenka, admin_ivanov, admin_petrov]

admins_logins_passwords_dict = {admin_haponenka.login: admin_haponenka.password,
                                admin_ivanov.login: admin_ivanov.password, admin_petrov.login: admin_petrov.password}


def log_in_admin(login, password):
    c = 3
    while c != 3:
        for k, v in admins_logins_passwords_dict.items():
            if k != login and v != password:
                print("Не корректные данные")
                c -= 1
            elif k != login and v == password:
                print("Не корректные данные")
                c -= 1
            elif k == login and v != password:
                print("Не корректные данные")
            else:
                print("Добро пожаловать в админ панель.\nЕсли вы хотите отобразить спсиок админов, введите - 1\n"
                      "Если хотите добавить админа, введите - 2\nЕсли хотите удалить админа, введите - 3 ")
                current_choice = input("Ваша выбор - ")
                main.func(current_choice)

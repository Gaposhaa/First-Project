import main
import receipts


class Information:

    def __init__(self, user_choice):
        self.user_choice = user_choice

    def getting_choice(self):
        if self.user_choice == "Сдаю в ремонт":
            print("""Приветствуем Вас в нашем сервисе по ремонту техники!
Пожалуйста, введите следующие данные:
                            - "Имя"
                            - "Очество"
                            - "Фамилия"
                            - "Тип техники(Телефон, Телевизор, Ноутбук)""")
            user_choice = main.Receipt(input("Имя - "), input("Очество - "),
                                       input("Фамилия - "), input("Тип - "))
            user_choice.filling_out_a_receipt()
        elif self.user_choice == "Информация":
            print("""Если Вас интересует информация о обращениях в наш сервис,
введите: "ФИО" в графе "Данные", для получения полной информации по обращениям, либо номер квитанции, для получения 
информации о конкретном обращении.""")
            current_data = input("Данные - ")
            if current_data == receipts.petrov_data:
                print(receipts.petrov_receipts_information)
            elif current_data == receipts.ivanov_data:
                print(receipts.ivanov_data_information)
            elif current_data == receipts.sergeev_data:
                print(receipts.sergeev_equipment_data_information)
            elif current_data == receipts.equipment_data_petrov.number_of_receipt:
                print(receipts.petrov_equipment_data_information)
            elif current_data == receipts.second_equipment_data_petrov.number_of_receipt:
                print(receipts.second_petrov_equipment_data_information)
            elif current_data == receipts.equipment_data_ivanov.number_of_receipt:
                print(receipts.ivanov_equipment_data_information)
            elif current_data == receipts.second_equipment_data_ivanov.number_of_receipt:
                print(receipts.second_ivanov_equipment_data_information)
            elif current_data == receipts.equipment_data_sergeev.number_of_receipt:
                print(receipts.sergeev_equipment_data_information)
            else:
                print("Данный пользователь не обращался в наш сервис. Либо введены не корректные данные")
        else:
            print("Введены не корректные данные")
            self.user_choice = input("Вводные данные(Сдаю в ремонт/Информация) - ")
            current_choice.getting_choice()


if __name__ == "__main__":
    print("""Уважаемый пользователь, выберите действие. "Сдаю в ремонт"(ввод данных о технике и описание поломки),
    "Информация"(Информация о обращениях в наш сервис) """)
    current_choice = Information(input("Вводные данные(Сдаю в ремонт/Информация) - "))
    current_choice.getting_choice()

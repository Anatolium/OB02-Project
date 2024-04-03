from random import randint

# Класс может предоставлять список сотрудников
class Company:
    def __init__(self, name):
        self.name = name
        self.__workers_list = []

    def get_workers_list(self, some_user):
        user_data = some_user.get_user_data()
        try:
            company = user_data[3].name
        except IndexError:
            # Список запросил объект класса User
            print(f"{user_data[1]} не имеет прав администратора\n")
            return None
        else:
            if company == self.name:
                return self.__workers_list
            else:
                print(f"У {user_data[1]} нет прав доступа к данным {self.name}\n")
                return None

class User:
    def __init__(self, name, access="user"):
        self.__id = randint(100000, 999999)
        self.__name = name
        self.__access = access

    def get_user_data(self):
        return self.__id, self.__name, self.__access

# Включает свойство 'company', которую он администрирует
class Admin(User):
    def __init__(self, name, company: Company):
        super().__init__(name, "admin")
        self.__company = company
        self.__admin_list = self.__company.get_workers_list(self)

    # Возвращаем дополнительно имя администрируемой компании
    def get_user_data(self):
        user_data = super().get_user_data()
        return user_data[0], user_data[1], user_data[2], self.__company

    def add_user(self, new_user):
        self.__admin_list.append(new_user)
        user_data = new_user.get_user_data()
        print(f"Пользователь {user_data[1]} с доступом '{user_data[2]}' добавлен в список сотрудников")

    def remove_user(self, name):
        for index, user in enumerate(self.__admin_list):
            user_name = user.get_user_data()[1]
            if user_name == name:
                self.__admin_list.pop(index)
                print(f"Пользователь {name} удалён из списка сотрудников")
                return
        print(f"Пользователь {name} не найден в списке сотрудников")

    def print_workers_list(self):
        if len(self.__admin_list) == 0:
            print("Список сотрудников пуст")
            return
        print(f"\nСписок сотрудников ({self.get_user_data()[1]}):")
        print("-"*44)
        for number, user in enumerate(self.__admin_list, 1):
            user_data = user.get_user_data()
            uid = user_data[0]
            name = user_data[1].ljust(24)[:24]
            access = user_data[2]
            print(f"{number}. {uid}  {name} {access}")
        print()

some_company = Company("Газпромбанк")
some_company.get_workers_list(User("Первый Встречный"))

admin = Admin("Администратор Иван", some_company)
admin.add_user(admin)
admin.add_user(User("Андрей Андреев"))
admin.add_user(User("Борис Борисов"))
admin.add_user(User("Макар Макаров"))
admin.add_user(User("Сергей Сергеев"))
admin.print_workers_list()

admin_2 = Admin("Администратор Олег", some_company)
admin_2.add_user(admin_2)
admin_2.remove_user("Макар Макаров")
admin_2.remove_user("Сергей Сергеев")
admin_2.add_user(User("Диана Дианова"))
admin_2.add_user(User("Марина Маринина"))
admin_2.print_workers_list()

admin_3 = Admin("Чужой Администратор", Company("Google"))
some_company.get_workers_list(admin_3)


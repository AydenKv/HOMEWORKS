from HomeWork4 import First, Second, Third, Fourth


class Fifth(Second, First, Third, Fourth):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.__age = age

    def print(self):
        super().print_smth()

    def print_2(self):
        super().print_smth2()

    @property
    def get_age(self):
        return self.__age

    @get_age.setter
    def set_age(self, num):
        self.__age = num
        return self.__age


a = Fifth('JAKE', 30)
print(a.name)
a.set_age = 50
print(a.get_age)


a.print()
a.print_2()

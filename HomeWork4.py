class First:
    def __init__(self, name):
        self.name = name


class Second(First):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


class Third:
    def print_smth(self):
        print('smth')


class Fourth:
    def print_smth2(self):
        print('smth2')

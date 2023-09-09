class SuperHero:
    people = 'people'
    damage = 1

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def print_name(self):
        print(self.name)

    def double(self):
        self.health_points *= 2
        return self.health_points

    def __str__(self):
        return f'nickname: {self.nickname}\nsuperpower: {self.superpower}\nHP: {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)

    def crit(self):
        self.damage **= 2
        return self.damage



class AirHero(SuperHero):
    people = 'people'
    damage = 40
    fly = False

    def double(self):
        self.health_points **= 2
        self.fly = True
        return self.health_points
    def true_phrase(self):
        print('True in the True_phrase')


class SpaceHero(SuperHero):
    people = 'people'
    damage = 50
    fly = False

    def double(self):
        self.health_points **= 2
        self.fly = True
        return self.health_points

    def true_phrase(self):
        print('True in the True_phrase')


class Villain(AirHero):
    people = 'monster'

    def gen_x(self):
        pass



# hero = SuperHero('JACK', 'RAVEN', 'TELEKINESIS', 100, 'Hasta la vista, baby')
# hero.print_name()
# hero.double()
# print(hero)
# print(len(hero))


air = AirHero('JAMES', 'AVATAR', 'AIR_CONTROL', 150, 'hello_world')
air.double()
air.crit()
print(air)
air.true_phrase()


space = SpaceHero('CHRIS', 'NICK', 'SPACE_CONTROL', 200, 'i am the one who knocks')
space.double()
air.crit()
print(space)
space.true_phrase()

villain = Villain('JAKE', 'MONSTER', 'BEING_MONSTER', 300, 'hello')
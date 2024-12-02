import random
from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

my_func = list(map(lambda x, y: x == y, first, second))
print(list(my_func))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        # write = get_advanced_writer('example.txt')
        # write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
        for file in file_name:
            with open(file, encoding='utf-8') as files:

    return write_everything()

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

from abc import ABC, abstractmethod
from random import randint


class Ishape(ABC):

    @abstractmethod
    def get_perimetr(self):
        # возврвщает периметр фигуры
        pass

    @abstractmethod
    def get_area(self):
        # возвращает площадь фигуры
        pass

    @abstractmethod
    def get_description(self):
        # возвращает произвольное описание
        pass


class Circle(Ishape):  # круг
    pi = 3.14

    def __init__(self, r):
        self.r = r

    def get_perimetr(self):
        return 2 * Circle.pi * self.r

    def get_area(self):
        return Circle.pi * (self.r ** 2)

    def get_description(self):
        return f'Я круг с радиусом {self.r}'


class Rectangle(Ishape):  # прямоугольник

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_perimetr(self):
        return (self.width + self.height) * 2

    def get_area(self):
        return self.width * self.height

    def get_description(self):
        return f'Я прямоугольник со сторонами {self.height}X{self.width}'


class Square(Ishape):  # квадрат

    def __init__(self, side):
        self.side = side

    def get_perimetr(self):
        return 4 * self.side

    def get_area(self):
        return self.side ** 2

    def get_description(self):
        return f'Я квадрат со стороной {self.side}'


class Game:
    QUESTION = 2

    def __init__(self):
        raise TypeError('Не может быть создан экземпляр данного класса')

    @staticmethod
    def __get_shape():
        random_digits = randint(1, 10)
        order_random = randint(1, 3)
        if order_random == 1:
            return Circle(random_digits)
        elif order_random == 2:
            return Rectangle(random_digits, random_digits)
        else:
            return Square(random_digits)

    @staticmethod
    def __calculate(string, answer):
        while True:
            guess = input(f'Укажите мою {string} :')
            if not guess.replace('.', '', 1).isdigit():
                continue
            if float(guess) == float(answer):
                print('Правильно')
                break
            else:
                print(f'Ошибка правильный ответ {answer}')
                break

    @classmethod
    def __run(cls):
        shape = cls.__get_shape()
        if isinstance(shape, Ishape):
            print(shape.get_description())
            cls.__calculate("площадь", shape.get_area())
            cls.__calculate("периметр", shape.get_area())
        else:
            raise TypeError

    @classmethod
    def play(cls):
        print(f'Привет!Мы геометрические фигуры и у нас есть {cls.QUESTION} вопроса.')
        while True:
            guess = input('Играем? Y/N:')
            if guess.upper() != 'Y':
                print('Спасибо за участие')
                break
            else:
                cls.__run()

Game.play()
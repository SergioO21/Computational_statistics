
import random


class Person:
    """  """
    def __init__(self, name):
        self.name = name


class TraditionalPerson(Person):
    """  """
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def walk():
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

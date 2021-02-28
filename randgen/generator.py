import randgen.libraries as libraries
import pkg_resources
import random


class Generator:
    def __init__(self, seed=None):
        self.__random = random.Random(seed) if seed else random.Random()

    def pick(self, population, n, unique=True):
        if unique:
            return self.__random.sample(population, k=n)
        else:
            return self.__random.choices(population, k=n)

    def number(self, min, max):
        '''Random number in [min, max]'''
        return self.__random.randint(min, max)

    def string(self, alphabet=None, min_length=0, max_length=100):
        alphabet = alphabet or libraries.lowercase_alphabet()
        length = self.__random.randint(min_length, max_length)
        return ''.join(self.pick(alphabet, length, unique=False))

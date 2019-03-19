# -*-coding:UTF-8 -*-
from enum import Enum, unique


class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


bart = Student('Bart', Gender.Male)
print(bart.gender == Gender.Male)
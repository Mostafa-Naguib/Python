from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name, gender, birthday, is_married):
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.is_married = is_married

    @abstractmethod
    def print_info():
        pass

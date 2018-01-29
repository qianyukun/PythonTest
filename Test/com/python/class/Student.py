class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    __slots__ = ('__name', '__age')

    def print_age(self):
        print self.__age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if 0 < age < 100:
            self.__age = age
        else:
            raise ValueError('age 0 ~ 100')

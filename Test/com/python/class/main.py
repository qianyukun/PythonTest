#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from Student import Student
from Dog import Dog
from IAnimalRunning import animal_running

s1 = Student('Jack', 19)
print s1.get_name()
s1.set_age(1)
# s1.set_age(-1)

dog = Dog()
dog.run()
dog.eat()

animal_running(dog)

print isinstance([1, 2, 3], (list, tuple))

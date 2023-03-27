import sys

class Person:
    temp = "Human"

    def __init__(self, name):
        self.name = name
        print(f"객체: {self}, 객체의 name: {self.name}, 클래스 변수: {Person.temp}")


man = Person("hwanseung")
women = Person("good")

print(man.temp, women.temp)
print(id(man.temp), id(women.temp))

global_variable = "Human"
print(id(man.temp), id(global_variable))


def local_function(x):
    a = "Human"
    print(f"local variable in function: {id(a)}, global variable: {id(global_variable)} ")
    return x ** 2

print(local_function(2))

print('\n\n')

global_variable = 15
print(f"global variable: {id(global_variable)}")


def local_function():
    a = 15
    print(f"local variable in function: {id(a)}")

local_function()
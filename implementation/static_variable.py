class Person:
    temp = "Human"

    def __init__(self, name):
        self.name = name
        print(f"객체: {self}, 객체의 name: {self.name}, 클래스 변수: {Person.temp}")


man = Person("hwanseung")
women = Person("good")

print(man.temp, women.temp)


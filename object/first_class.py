import sys


class Person:
    number_of_instances = 0

    def __init__(self, name: str, age=17) -> None:
        self._name = name
        self._age = age
        Person.number_of_instances += 1

    @classmethod
    def get_number_of_instances(cls):
        return cls.number_of_instances

    @staticmethod
    def determine_class(age: int) -> str:
        if age >= 18:
            return 'Major'
        return 'Minor'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) < 1:
            return
        self._name = name

    @name.deleter
    def name(self):
        print('name will be deleted')
        del self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise ValueError("age can't be negative")
        self._age = new_age


person = Person("obi")

person.name = "chukwudi"
# del person.name

print(person.determine_class(person.age))

try:
    print(person.age)
except:
    print("Oops!", sys.exc_info()[0], "occurred.")

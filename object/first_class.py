class Person:

    def __init__(self, name: str) -> None:
        self._name = name

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
        self._name = ''


person1 = Person("obi")

person1.name = "chukwudi"
del person1.name
print(person1.name)

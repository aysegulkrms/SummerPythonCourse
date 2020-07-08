class Person:

    def __init__(self, f_name, age):
        self.f_name = f_name
        self._age = age

    def show_age(self):
        return self._get_age()

    def _get_age(self):  # here the function is private and can't be accessed externally
        return self._age


person_1 = Person("Michael", 35)
print("Age is", person_1.show_age())



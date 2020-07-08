class Person:

    def __init__(self, f_name, email, age):
        self.f_name = f_name  # public variable
        self._email = email  # private variable (_string)
        self._age = age  # the private variable is used only internally

    def get_email(self):
        return self._email

    def update_email(self, email):
        self._email = email

    def get_age(self):
        return self._age


person_1 = Person("Jack", 'jack@sample.com', 30)
print(person_1.f_name, person_1.get_email())
person_1.update_email("jack@gmail.com")
print(person_1.get_email())
print(person_1.get_age())
# create private age variable inside the init function
# create a get_age function

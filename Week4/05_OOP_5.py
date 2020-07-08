class Developer:

    def __init__(self, first_name, last_name, phone, salary, programming_lang):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.salary = salary
        self.programming_lang = programming_lang

    def info(self):
        print("""
Developer information:

Name : {0}
Last Name : {1}
Phone : {2}
Salary : {3}
Programming Languages : {4}

        """.format(self.first_name, self.last_name, self.phone, self.salary, self.programming_lang))


developer_1 = Developer("Cemil", "Koc", 6789087684, 5000, ["Python", "Java", "SQL", "Groovy"])

# print(developer_1.first_name)
# print(developer_1.last_name)
# Shift + tab unindentation


developer_1.info()




class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def information(self):
        print("{} {} earns {}".format(self.first, self.last, self.pay))


emp_1 = Employee("Mike", "Schafer", 4200)
emp_2 = Employee("Cemil", "Koc", 3500)

# emp_1.first = "Mike"
# emp_1.last = "Scafer"
# emp_1.pay = 4200

# emp_2.first = "Cemil"
# emp_2.last = "Koc"
# emp_2.pay = 3500

# print(emp_1.first + ' ' + emp_1.last, emp_1.pay)
# print(emp_2.first + ' ' + emp_2.last, emp_2.pay)

emp_1.information()
emp_2.information()

class Employee:

    raiseAmount = 1.04
    no_of_emp = 0
    raiseAmount2 = 2.00

    def __init__(self, first, last, pay):
        self.fname = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay
        Employee.no_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.fname, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raiseAmount)

    def apply_raise2(self):
        self.pay = int(self.pay * Employee.raiseAmount2)


class Developer(Employee):
    '''
    If we try to access the data (or) method from this sub class Python will search that in the sub class first
    if it is not there it will search in its super class .This is called Method resolution

    Method resolution order:
 |      Developer
 |      Employee
 |      builtins.object
    '''
    raiseAmount2 = 4.00

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        '''
        We can also use Employee.__init__(self,first,last,pay) ,both works the same way
        But super() method is enough for single inheritance
        '''
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        # Mutable items should not be passed as default arguments
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("--->", emp.fullname())


dev1 = Developer('Mothish', "MC", 50000, "Python")
dev2 = Employee("Hsihtom", "CM", 60000)

print(help(Developer))
print("\n-------------------------\nBefore raising the pay,")
print(dev1.pay)
print(dev2.pay)
print("After raising the pay,")
dev1.apply_raise()
dev2.apply_raise()
print(dev1.pay)
print(dev2.pay)
print("-------------------------")

print("\n-------------------------\nBefore raising the pay,")
print(dev1.pay)
print(dev2.pay)
print("After raising the pay,")
dev1.apply_raise2()  # here the subclass itself has raiseAmount2 attribute so it only has effect in subclass attribute alone
dev2.apply_raise2()
print(dev1.pay)
print(dev2.pay)
print("-------------------------")

print(dev1.prog_lang)

mgr1 = Manager("Sue", "Smith", 90000, [dev1])
mgr2 = Manager("Smith", "Sue", 90000)
mgr1.print_emps()
mgr2.print_emps()

print("After adding..")
mgr1.add_emp(dev2)
mgr2.add_emp(dev1)
mgr1.print_emps()
mgr2.print_emps()

print("After removing..")
mgr1.remove_emp(dev1)
mgr1.remove_emp(dev2)
print("For manager 1")
mgr1.print_emps()
print("For manager 2")
mgr2.print_emps()

# Builtin methods
print("\n\n Method: isinstance()")
print(isinstance(mgr1, Manager))
# returns true coz manager is a subclass of employee
print(isinstance(mgr1, Employee))
print(isinstance(mgr1, Developer))
print("\n\n Method: issubclass()")
print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))

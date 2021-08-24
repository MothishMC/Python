import datetime


class Employee:
    '''
    Static methods are the methods ,which don't take any instance or class as their first argument
    They behave as normal regular function
    They are included to class because they are logically related to that class
    '''

    raiseAmount = 1.04
    no_of_emp = 0

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

    # to make regular method to class method add decorator to it
    @classmethod
    def set_raiseAmount(cls, amount):
        '''
        Silimar to regular methods , we use cls by the common convention (we can't use class as it is a keyword)
        '''
        cls.raiseAmount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        # this will instantiate new object of this class
        return cls(first, last, pay) ### If we don't use cls here in this method then we can define that method as static

    @staticmethod
    def isWorkDay(day):  # no cls or self as first argument
        # In python weekdays enumerated like Monday as 0 ....Sunday as 6
        if day.weekday() in (5, 6):
            return False
        else:
            return True


print(f"raiseAmount={Employee.raiseAmount}")
emp1 = Employee('Mothish', "MC", 50000)
emp2 = Employee("Hsihtom", "CM", 60000)
Employee.set_raiseAmount(1.05)  # equivalent to Employee.raiseAmount=1.05
# We can class methods by instances as well (ex: emp1.set_raiseAmount(1.05)),but it is not preferable
print("-----------------------")
print(Employee.raiseAmount)
print(emp1.raiseAmount)
print(emp2.raiseAmount, end='\n-----------------------\n')

emp_str_1 = "MC-Mothish-50000"
emp_str_2 = "CM-Hsihtom-60000"

new_emp_1 = Employee.from_string(emp_str_1)  # Alternative constructor
new_emp_2 = Employee.from_string(emp_str_2)

print(new_emp_1.email)
print(new_emp_2.pay)

mydate = datetime.date(2021, 4, 11)
mydate1 = datetime.date(2021, 4, 8)

print(Employee.isWorkDay(mydate))
print(Employee.isWorkDay(mydate1))

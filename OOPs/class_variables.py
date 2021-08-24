# class variables are the variables that are shared among all the instances
class Employee:
    '''
    When we access class variable , we need to access them through either the class itself or the instance
    Ex : class.Classattribute (or) instance.Classattribute
    '''
    raiseAmount = 1.04
    raiseAmount2 = 2.04
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
        '''
         (or) self.pay = int(self.pay * Employee.raiseAmount)
         if we self.pay =int(self.pay * raiseAmount) throws a NameError: name 'raiseAmount' is not defined
        '''

    def apply_rasie2(self):
        self.pay = int(self.pay * Employee.raiseAmount2)


print(
    f"-----------------\nNo.of.Employee : {Employee.no_of_emp}\n-----------------\n")

emp1 = Employee('Mothish', "MC", 50000)
emp2 = Employee("Hsihtom", "CM", 60000)
print("After instantiating,")
print(
    f"-----------------\nNo.of.Employee : {Employee.no_of_emp}\n-----------------\n")
print(emp1.__dict__)
'''
Output : {'fname': 'Mothish', 'last': 'MC', 'email': 'Mothish.MC@company.com', 'pay': 50000} , here we don't have attribute raiseAmount
'''
print(Employee.__dict__)
'''
Output:
{'__module__': '__main__', 'raiseAmount': 1.04, '__init__': <function Employee.__init__ at 0x000001E82992ACA8>,
'fullname': <function Employee.fullname at 0x000001E829A7A288>, 'apply_raise': <function Employee.apply_raise at 0x000001E829A72F78>,
'__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}
Here the class have the attribute
'''
# block-0
print(Employee.raiseAmount)
print(emp1.raiseAmount)
print(emp2.raiseAmount, end='\n\n')

# block-1
Employee.raiseAmount = 1.05  # will change the value , reflects in all the instances

print(Employee.raiseAmount)
print(emp1.raiseAmount)
print(emp2.raiseAmount, end='\n\n')
print(emp1.__dict__)
'''
Output : {'fname': 'Mothish', 'last': 'MC', 'email': 'Mothish.MC@company.com', 'pay': 50000} ,still we don't have  raiseAmount
'''
# block-2
# will only change the value for its instance (emp1) alone
emp1.raiseAmount = 1.06

print(Employee.raiseAmount)
print(emp1.raiseAmount)
print(emp2.raiseAmount, end='\n\n')
print(emp1.__dict__)
'''
Output : {'fname': 'Mothish', 'last': 'MC', 'email': 'Mothish.MC@company.com', 'pay': 50000, 'raiseAmount': 1.06} , now he have raiseAmount
'''
'''
Output for block 0: 1.04 1.04 1.04
Output for block 1: 1.05 1.05 1.05
Output for bock  2: 1.05 1.06 1.05

Explaination :
When we modify the class variable with instance (ex: emp1.raiseAmount) ,
         it will include that class-Attribute within the namespace of that instance

When we access the class varible in main with instance identity ,it will search that attribute in it's namespace
        if it is there it will return else it will search in the class
Hence after the statement emp1.raiseAmount=1.06 , it has the attribute in its namespace so it returns 1.06
And the using of 'self' to the attribute  raiseAmount in apply_method() allow that instance to override its value in its  namespace
'''
# block-3
Employee.raiseAmount2 = 2.05
print("Block-3")
print(Employee.raiseAmount2)
print(emp1.raiseAmount2)
print(emp2.raiseAmount2)
print(emp2.__dict__, end='\n\n')
# block-4
emp2.raiseAmount2 = 3.10
print("Block-4")
print(Employee.raiseAmount2)
print(emp1.raiseAmount2)
print(emp2.raiseAmount2)
print(emp2.__dict__, end='\n\n')

'''
Output:
Block-3
2.05
2.05
2.05
{'fname': 'Hsihtom', 'last': 'CM', 'email': 'Hsihtom.CM@company.com', 'pay': 60000}

Block-4
2.05
2.05
3.1
{'fname': 'Hsihtom', 'last': 'CM', 'email': 'Hsihtom.CM@company.com', 'pay': 60000, 'raiseAmount2': 3.1}
'''

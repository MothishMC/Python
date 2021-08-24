"""
    Magic methods in Python are the special methods that start and end with the double underscores.
    They are also called dunder [Double UNDER (underscore)] methods.
    Magic methods are not meant to be invoked directly by you,
        but the invocation happens internally from the class on a certain action.
            eg: when you add two numbers using the + operator, internally, the __add__() method will be called.

    Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.

    Built-in classes in Python define many magic methods.
    Use the dir() function to see the number of magic methods inherited by a class.

    These methods are the reason we can add two strings with ‘+’ operator without any explicit typecasting.

    1) These methods allow us to emulate (reproduce the function or action of ) some built-in behavior within python.
    2) These are commonly used for operator overloading.

"""

class Employee:

    def __init__(self, first, last, pay):
        self.fname = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.fname, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raiseAmount)

    def __repr__(self):
        # Defined to produce a string (python code)  that can be copy and paste  to reproduce the Object
        return "Employee('{}','{}',{})".format(self.fname, self.last, self.pay)

    def __str__(self):
        return f"Full name :{self.fullname()} - Email : {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        # try to return the length of full name
        return len(self.fullname())


emp1 = Employee('Mothish', "MC", 50000)
emp2 = Employee("Hsihtom", "CM", 60000)

"""
    print(emp1)
    print(emp2)
    print(str(emp1)) ==> equivalent to print(emp1.__str)
    print(str(emp2))
    print(repr(emp1))
    print(repr(emp2))

    // No defined repr and str
   Output:

    <__main__.Employee object at 0x000002003AD1AC08>
    <__main__.Employee object at 0x000002003AD1AC48>
    <__main__.Employee object at 0x000002003AD1AC08>
    <__main__.Employee object at 0x000002003AD1AC48>
    <__main__.Employee object at 0x000002003AD1AC08>
    <__main__.Employee object at 0x000002003AD1AC48>


object.__repr__(self)

    Called by the repr() built-in function to compute the “official” string representation of an object.
    If at all possible, this should look like a valid Python expression that could be used to recreate
        an object with the same value (given an appropriate environment).
    If this is not possible, a string of the form <...some useful description...> should be returned.
    The return value must be a string object.
    If a class defines __repr__() but not __str__(),
        then __repr__() is also used when an “informal” string representation of instances of that class is required.

    This is typically used for debugging, so it is important that the representation is information-rich and unambiguous.

object.__str__(self)

    Called by str(object) and the built-in functions format() and print()
        to compute the “informal” or nicely printable string representation of an object.
    The return value must be a string object.
    This method differs from object.__repr__() in that there is no expectation
        that __str__() return a valid Python expression: a more convenient or concise representation can be used.

    The default implementation defined by the built-in type object calls object.__repr__().


==> __repr__() meant for  things like debugging ,logging etc ,this will be used by developers
==> __str__()  meant for  readable representation ,end users

"""

print(emp1)
print(repr(emp1))
print(emp1.__str__())

print("\n----------------------------------------------------")
print(1 + 2)
print(f"Actual process will be int.__add(1,2){int.__add__(1,2)}")
print("a" + "b")
print(f"Actual process will be int.__add(1,2){str.__add__('a','b')}")
print("----------------------------------------------------")

'''
Before defining the dunder add for this class ,

print(emp1 + emp2)
Output:
    TypeError: unsupported operand type(s) for +: 'Employee' and 'Employee'
Reason:
     because this '+' doesn't know what to do with those

print(len(emp1))
Output:
    TypeError: object of type 'Employee' has no len()
Reason:
    This Class has no method called len() untill we define it
'''
print(emp1 + emp2)
print("\n----------------------------------------------------")
print(len('Type'))
print(f"The length of the employee : {len(emp1)} including spaces")

"""
Real_time examples:
    Check in datetime.py module
        1) find __add__()
            NotImplemented --> means that function doesn't have anything to handle the error
                it will just pass that error to the parent function .if that parent dosen't have any mechanism to handle the error
                    it will definitelt throw errors
        2) find class date
                check __repr__()
                check __str__
"""


prjbrkjabfkjbfbkbkbkabfdiyl
prjbrkjabfkjbfbkbkbkabfdiyl
prjbrkjabfkjbfbkbkbkabfdiyl
prjbrkjabfkjbfbkbkbkabfdiyl
prjbrkjabfkjbfbkbkbkabfdiyl


mcbsdkbk


mcbsdkbk

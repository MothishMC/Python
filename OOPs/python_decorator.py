"""
class Employee:

    def __init__(self, first, last):
        self.fname = first
        self.last = last
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.fname, self.last)


emp1 = Employee("Mothish", "MC")
print("Before update : ")
print(emp1.fullname())
print(emp1.fname)
print(emp1.email)
print("-------------------------\nAfter Update")
emp1.fname = "Hishtom"
print(emp1.fullname())
print(emp1.fname)
print(emp1.email)

Output:
Before update :
Mothish MC
Mothish
Mothish.MC@company.com
-------------------------
After Update
Hishtom MC
Hishtom
Mothish.MC@company.com

Reason:
   email will not change even after we update but the full name will change Coz whenver we call the fullname()
   it will take the current instance of first & last name of that class

Soln:
    like fullname() method we can have email as method but it will break the code fot them ,whoever uses our class as they
have to change the email attribute to email() method wherever they use it. So we have to retain the email method as attribute
by using property decorators.


"""
class Employee:

    def __init__(self, first, last):
        self.fname = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.fname, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.fname, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.fname = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Name Deleted!!")
        self.fname = None
        self.last = None


emp1 = Employee("Mothish", "MC")
print("Before update : ")
print(emp1.fullname)
print(emp1.fname)
print(emp1.email)
print("-------------------------\nAfter Update")
emp1.fname = "Hishtom"
print(emp1.fullname)
print(emp1.fname)
print(emp1.email)
print("-------------------------\nAfter fullname Update")
emp1.fullname = "MC Mothish"
print(emp1.fullname)
print(emp1.fname)
print(emp1.email)
print("-------------------------")
del emp1.fullname
print(emp1.fname)
print(emp1.last)
'''
Summary:
1) Property decorators allow us to use the attribute without using getter and setter everywhere
2) People who user class no need to change their code because they can still use the attribute like they used before
(if people already use our class)
'''

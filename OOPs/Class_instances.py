# class          --> blueprint
# Object         -->  instance
# class data     --> Attributes
# class function --> methods

class Employee:
    '''
    When we Create a method inside a Class ,by default ,it takes the instance as its first argument
    '''
    # Initialize -Similar to constructor

    def __init__(self, first, last, pay):
        # By convention ,we use self (can be any name) for instance
        # Unlike Java , eventhough we use different name for attributes we have to use self.attribute
        self.fname = first
        #[ self is not like this reference  in JAVA]
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.fname, self.last)
    '''
    if we not pass self to the method
    def fullname(self):
        return '{} {}'.format(self.fname, self.last)

    Code : instance.fullname()

    Output : TypeError: fullname() takes 0 positional arguments but 1 was given

    Reason : while calling a method , the method takes the calling instance as it's first argument
    '''


emp1 = Employee('Mothish', 'MC', 50000)

print(emp1.fname)
print(emp1.email)
Name = emp1.fullname()  # to differentiate b/w attribute and method we should use ()
# if we forget to put () , this method will return only the methid not the  values
print(emp1.fullname)
print(Name)
# we can also this way to call the method of class
Name1 = Employee.fullname(emp1)
''' note the above method of calling a method compulsory requires 1 argument (the instance)
    without that ,it is meaning less & again throws an error
    TypeError: fullname() missing 1 required positional argument: 'self' .
    thar's why we have 'self' as parameter in the methods
'''
print(Name1)
'''
Explaination for this TypeError: fullname() takes 0 positional arguments but 1 was given :

When we call a method for emp1 says emp1.fullname() it will get transform to Employee.fullname(emp1) in background
'''

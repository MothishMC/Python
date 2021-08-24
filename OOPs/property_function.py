"""
In Python, the main purpose of Property() function is to create property of a class.

    Syntax: property(fget, fset, fdel, doc) or property(fget=None, fset=None, fdel=None, doc=None) or property(fget, fset, fdel,)

    Parameters:
    fget() – used to get the value of attribute
    fset() – used to set the value of attribute
    fdel() – used to delete the attribute value
    doc() – string that contains the documentation (docstring) for the attribute

    Return: Returns a property attribute from the given getter, setter and deleter.

Return value from property() :

    property() returns the property attribute from the given getter, setter, and deleter.

        If no arguments are given, property() returns a base property attribute that doesn't contain any getter, setter or deleter.
        If doc isn't provided, property() takes the docstring of the getter function.

"""


class Person:
    def __init__(self, name):
        self._name = name  # _name private variable

    # getter method for getting the value
    def get_name(self):
        print('Getting name')
        return self._name
    # setter method for assigning the value

    def set_name(self, value):
        print('Setting name to ' + value)
        self._name = value

    # deleter method to delete the value
    def del_name(self):
        print('Deleting name')
        del self._name

    # Set property to use get_name, set_name
    # and del_name methods
    # we set a new property attribute name by calling the property() method.
    name = property(get_name, set_name, del_name, 'Name property')


p = Person('Adam')
print(p.name)
p.name = 'John'
del p.name
"""
Notice that the same method name() is used with different definitions for defining the getter, setter and deleter.
 Whenever we use p.name, it internally calls the appropriate getter, setter and deleter.
"""

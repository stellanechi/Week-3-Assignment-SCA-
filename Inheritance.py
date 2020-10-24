# Create a class named Person
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    # this is a method
    def printname(self):
        print(self.firstname, self.lastname)


# Use the Person class to create an object, and then execute the printname method:

x = Person("Stella", "Obasanjo")
x.printname()


# Create a class named Student, which will inherit the properties and methods from the Person class

class Student(Person):
    pass


x = Student("Mike", "Olsen")
x.printname()

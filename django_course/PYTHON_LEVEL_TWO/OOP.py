# print(type(''))
# print(type(2))
# print(type(True))
# print(type([]))
# print(type({}))
# print(type(()))
# class Sample():
#     pass
# x = Sample()
# print(type(x))

#class


class Dog():
    # CLASS OBJECT ATTRIBUTE
    species = "mammal"
    #INITIALIZATION
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

mydog = Dog("Lab","Sammy")


#class with methods
class Circle():
    pi = 3.14
    def __init__(self, radius=1):
        self.radius = radius
    def area(self):
        return self.radius*self.radius * Circle.pi
    def setRadius(self, new_radius):
        self.radius = new_radius
myc = Circle(3)
myc.setRadius(100)


#inheritance


# class Animal():
#     def __init__(self):
#         print("Animal Created")
#
#     def whoAmI(self):
#         print("ANIMAL")
#     def eat(self):
#         print('EATING')
#
# class Dog(Animal):
#     def __init__(self):
#         print('Dog Created')
#     def eat(self):
#         print('Dog Eating')
#     def bark(self):
#         print('Woof!')
#
# mydog = Dog()
# mydog.whoAmI()
# mydog.eat()
# mydog.bark()




#special methods

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)
    def __len__(self):
        return self.pages
    def __del__(self):
        print('A book has been destroyed')
b = Book("Python", "Jose", 200)
print(b)
print(len(b))
del b
mylist = [1,2,3]
print(mylist)

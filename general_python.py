% Decorators
% can be used to modify a function and to perform custom code before and after.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator # @my_decorator is an easier way of saying "say_whee = my_decorator(say_whee)"
def say_whee():
    print("Whee!")
    

# >>> say_whee() yields:
Something is happening before the function is called.
Whee!
Something is happening after the function is called.



attribute self
Attribute self is used in method to receive the intstance of the class inside a method. Self is passed automatically to methods in python, but not received automatically. 

e.g.
  class food():

    # init method or constructor
    def __init__(self, fruit, color):
    self.fruit = fruit
    self.color = color

    def show(self):
    print("fruit is", self.fruit)
    print("color is", self.color )

    apple = food("apple", "red")
    grapes = food("grapes", "green")

    apple.show()
    grapes.show()
    
self.cache

magic methods
are defined internally in python, but can be overwritten. E.g. __init__() most common magic methodd

class Person:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
  #overriding magic method
  def __gt__(self, other):
    return self.salary > other.salary

obj1 = Person('John', 4500)
obj2 = Person('Natasha', 6000)
print(obj1.name, 'earns more than', obj2.name, '-', obj1 > obj2)
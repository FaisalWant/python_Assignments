"""def inc(x):
     return x+1

def dec(x):
     return x-1

def operate(func, x):
     result=func(x)
     return result
x=10
print(operate(inc,x))
print(operate(dec,x))


def make_pretty(func):
    def inner():
         print("i got decorated")
         func()  # this this the inputted function
    return inner
def ordinary():
    print("I am ordinary")


#ordinary()
pretty= make_pretty(ordinary)
pretty()


def smart_divide(func):
     def Inner(a,b):
          print("I am going to divide ", a, "and", b)
          if b==0:
              print("whoops cannot divide")
              return
          return func(a,b)
     return Inner

@smart_divide
def divide(a,b):
       return a/b
takeme= smart_divide(divide)
takeme(3,4)

def debug(function):
    def wrapper(*args, **kwargs):
        print("Arguments:", args, kwargs)
        return function(*args, **kwargs)
    return wrapper

def foo(a, b,c=1):
    return(a+b)*c
foo= debug(foo)
foo(2,3)
foo(2,3,c=1)

class Complex:


    \""" A simple example class\"""
    num= 12345
    def greet(self):
          return "hello world"

x=Complex()
print(type(x.greet))  #only variable got accessed
print(type(Complex.greet))
print(x.num is Complex.num)
print(x.greet is Complex.greet)

class Complex:
    def __init__(self, realpart=0, imagpart=0):
        self.real= realpart
        self.imag= imagpart
    def greet(self):
         print("Real :", self.real)
         print("Imaginary:", self.imag)

c= Complex(3,-4.5)
c.greet()
c.real=9
c.imag=4.5
c.greet()
c.greet()

class MyOtherClass:
    num=12345
    def __init__(self):
        self.num=1


x= MyOtherClass()
print(x.num)
del x.num   #over rides the  value initialized by the constructor
print(x.num)

class Pizza:
      def __init__(self, radius, toppings, slices=8):
          self.radius= radius
          self.toppings= toppings
          self.slices_left= slices
      def eat_slices(self):
          if self.slices_left>0:
               self.slices_left-=1
          else:
              print("Oh no! sorry pal out of pizzas")
      def __repr__(self):
           return\ '{} pizza '.format(self.radius)
p= Pizza(14, ("Pepperoni","olives"), slices=12)
print(Pizza.eat_slices)
print(p.eat_slices)
method= p.eat_slices
print(method.__self__)
print(method.__func__)

class Dog:
    kind = 'Canine'  # class variable shared by all instance variable
    def __init__(self, name):
        self.name= name    #instance variable unique to each instance variable
a= Dog('Astro')
print(a.name)
pb= Dog("Mr Smurfy")
print(pb.name)
print(a.kind)
print(pb.kind)
print(Dog.kind)
print(name.__self__)


class Dog:
    tricks=[]
    def __init__(self, name):
        self.name=name
    def add_trick(self, trick):
        self.tricks.append(trick)
d= Dog('Fido')
e= Dog('buddy')
d.add_trick('roll Over')
e.add_trick('play dead')
print(d.tricks)


class Dog:
    \""" Problem:
     even thought tricks at first appeard to be unique to a particular
    instance it  is not\"""
    def __init__(self, name='',tricks=[]):
        self.name= name
        self.tricks= tricks

    def add_trick(self, trick):
        self.tricks.append(trick)

d= Dog('Fido')
e= Dog('Buddy')

d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
""""
class Dog :

    def __init__(self, name):
        self.name= name
        self.tricks=[]  #New list for each Dog
    def add_tick(self, trick):
        self.tricks.append(trick)

d= Dog('Fido')
e=Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)

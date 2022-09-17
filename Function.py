# Basic simple Function

from tkinter import Y
from unittest import result


def greeting():
    print("Namaste")
    print("Have a nice day")

greeting() #calling the function

greeting()# In Python we can call a function as many times as we want.....

#Function With Arguments also called Patameters

def person(name,age): # Here are two arguments  inside the brcess in this function
    print("My name is " + name)
    print("And My age is " + str(age))
person("Sudip",22) # passing the value

# Types argument 

def add(x,y): # Formal argument
    z=x+y 
    return z #returning the valu 

result=add(20,30) #actual argument
print("sum = " + str(result)) 

#passing multiple value in limited parameter

def sub(a ,*b): # in here * symbol is used to implement to variable length argument
    c=a 
    for i in b:
        c=c-i 
        print(c)

sub(9,7,6,5,4) # variable length argument

# keyword variable length

def Details(name, **data):
    print(name)
    print(data)

Details("Ashik", Age=22, City="ktm") # in here age and city are keyworded variable length..

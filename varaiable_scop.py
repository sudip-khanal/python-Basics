
from re import X


a=10 #global variable
def somthing():
    a=5 #local variable
    print("In function " +str(a))#printing variable from function
somthing()  

print("outside function " +str(a))#print a from outside from function

#global variable in side function

x=100
def test():
    global x 
    x=50
    print("inside function " +str(x))
test()
print("outside " +str(x))
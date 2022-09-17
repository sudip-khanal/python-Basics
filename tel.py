#introduction to function
"""
def greet():
    print("Hello")
    print("world")

greet()
greet()

"""

#calculation

def calculation(x,y):
    a=x+y
    b=x-y
    c=x*y
    d=x/y
    
    return a,b,c,d

result1,result2,result3,result4 = calculation(7,9)
print( "X+Y= " +str(result1))
print("X-Y= "  +str(result2)) 
print("X * Y= " +str(result3)) 
print("X/y= " +str(result4))  




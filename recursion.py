# Recursion 
# By defualt python repeat to 1000 times

import sys
print(sys.getrecursionlimit())

#we can set the limit as we want
sys.setrecursionlimit(200)
print(sys.getrecursionlimit())


# Calculating factorial using recursion
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

result=fact(int(input("Enter The Number To Find the factorial:")))
print("Factorial of given Number is:",result)
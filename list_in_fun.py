# Passing  List to the Functin

#count the even number and odd number in the list

lst=[20,40,90,60,55,84,67,43,56,76,43,88,66]
def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
         even+=1
    else:
        odd+=1
        return even,odd
even,odd=count(lst)

print("Number of Even Number in List:{} and Number of Odd Number in List:{}".format(even,odd))

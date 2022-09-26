#List is the sequence of Element of any data type and mutable

lis=["Hi","Good ","morning"]
print(type(lis))
print(len(lis))


list1=[1,2,"Hello",2.3,"laptop","school"]
print(list1)
#indexing 
print(list1[0],list1[4])
#slicing
print(list1[1:4])
print(list1[:5])
print(list1[4:])


# let's Modify the content of list

animals=["Tiger","Elephant","Rhino","Jackle","Dog"]
print(animals)
#using append method to add an element to the list
animals.append("cat")
print(animals)

#insert method 
animals.insert(0,"Apple")# here 0 is index 
print(animals)

#removing method

animals.remove("Apple")
print(animals)

#Another way to remove the element of the list is pop()method

animals.pop(3)
print(animals)

# list are mutable so we can modify or change the value also
animals[0]="cow"
print(animals)


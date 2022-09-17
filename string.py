#string is a data type in python 
name="sudip"
print(name)

#string indexing 
name="sudip khanal"
print(name[0])
print(name[10])
#negative indexing
print(name[-1])
print(name[-2])

#slice : the portion of a string that can contain more than one character also somethime called a substring
color="orange"
print(color[1:4])
print(color[:4])
print(color[4:])

#different method of string

animals="Tiger,Dog and Cat"
print(animals.index("D"))
print(animals.index("Cat"))
print(animals.index("T"))

# upper () and lower () method

name="mount_everest"
print(name.upper())

print("APPLE".lower())


#count method

para="The is a python programming language"
print(para.count("a"))
print(para.count("i"))
print(para.count("s"))

#endwith method
paragraph="The is a python programming language"
#print(paragraph.endwith("h"))

#join method

test= " ".join(["this",     "is","a ","code","editor"])
print(test)

demo="...".join(["this",     "is","a ","code","editor"])
print(demo)


#splite method

a= "visual studio code is a code editor".split()
print(a)


##string formating 

name ="sudip"
age= 22

print("My name is {}, my age is{}".format(name,age))
##another example 
print("your age is {age} and your name is {name}".format(age=age,name=name))


#is numeric method
print("12343".isnumeric())
print("dfghj".isnumeric())
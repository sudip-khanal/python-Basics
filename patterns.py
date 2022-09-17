#printing different typeds of patterns
"""
for i in range(4):
    for j in range(1+i):
        print("#",end=" ")
    print()
"""

"""num=5
for i in range(4):
    for j in range(4-i):
        
        print(num, end=" ")
        num=num
    print()"""

num=1
row=int(input("Enter the rows"))
col=int(input("Enter the columns"))
for i in range(row):
    for j in range(col):
        print(num,end=" ")
        num=num+1
    print()


#fibonacci numbers 
#sequence of fibonacci number 0 1 1 2 3 5 8 13 21 
#the seuence is: 0,1,0+1=1,1+1=2,1+2=3,2+3=5,3+5=8,5+8=13



def fibonacci(n):
	a = 0
	b = 1
	
	# Check is n is less than 0
	if n <= 0:
		print("Incorrect input")
		
	
	# Check if n is equal to 1
	elif n == 1:
		return b
	else:
		for i in range(1, n):
			c = a + b
			a = b
			b = c
		return b

# Driver Program

Result=(fibonacci(int(input("Enter the Number For Fibonacci:"))))
print("Fibonacci number of given number:", Result)



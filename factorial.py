##Factorial

##Using in-build funtion
import math
n=int(input())
print(math.factorial(n))


##without using in-build funtion
def factorial(d):
	if d != 1:
		return d*factorial(d-1)
	else:
		return 1	

n=int(input())
if n != 0:
	print(factorial(n))
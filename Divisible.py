##You are given an array  of size  that contains integers. Here,  is an even number. You are required to perform the following operations:
##Divide the array of numbers in two equal halves
##Note: Here, two equal parts of a test case are created by dividing the array into two equal parts.
##Take the first digit of the numbers that are available in the first half of the array (first 50% of the test case)
##Take the last digit of the numbers that are available in the second half of the array (second 50% of the test case)
##Generate a number by using the digits that have been selected in the above steps

##Using below rule -
##A number is said to be divisible by 11 if the difference between the sum of the digits at the alternative places 
##starting from the left or the right is either 0 or a number that is divisible by 11
n=int(input())
a=list(map(int,input().split()))
sumEven=0
sumOdd=0
for i in range(len(a)):
	if i < (len(a)/2):
		while a[i] > 10:
			a[i]//=10
	else:
		a[i]%=10		
for i in range(len(a)):
	if i%2==0:
		sumEven+=a[i]
	else:
		sumOdd+=a[i]
diff = sumEven-sumOdd
if (diff == 0 | diff%11==0): 
	print("OUI")
else:
	print("NON")
	

n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
	if i < (len(a)/2):
		while a[i] > 10:
			a[i]//=10
	else:
		a[i]%=10
num=int("".join(map(str,a)))
if (num%11==0): 
	print("OUI")
else:
	print("NON")
		

##Using string manipulation

n=int(input())
a=input().split()
num="".join([a[i][0] for i in range(n//2)])+"".join([a[i][-1] for i in range(n//2,n)])

if (int(num)%11==0): 
	print("OUI")
else:
	print("NON")



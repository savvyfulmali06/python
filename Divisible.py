##You are given an array  of size  that contains integers. Here,  is an even number. You are required to perform the following operations:
##Divide the array of numbers in two equal halves
##Note: Here, two equal parts of a test case are created by dividing the array into two equal parts.
##Take the first digit of the numbers that are available in the first half of the array (first 50% of the test case)
##Take the last digit of the numbers that are available in the second half of the array (second 50% of the test case)
##Generate a number by using the digits that have been selected in the above steps


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
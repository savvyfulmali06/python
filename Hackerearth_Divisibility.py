n = int(input())
a=list(map(int,input().split()))

num=[a[i]%10 for i in range(len(a))]

num = int("".join(map(str,num)))

if (num % 10 == 0):
	print("Yes")
else:
	print("No")

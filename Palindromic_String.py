##Palindromic String

n=input().lower()
c=0
for i in range(len(n)//2):
	if n[i] != n[-i-1]:
		c+=1
		break;
if c==0:
	print("YES")
else:
	print("NO")
	

n=input().lower()
r=n[::-1]
if (n == r):
	print("YES")
else:
	print("NO")

	

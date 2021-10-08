## Count number of zoo
## 2 * x = y where z is x & o is y
## example input zzzoooooo ; 3z & 6 O;  2 * 3x = 6 y

s=input()
x=[]
y=[]
for i in range(len(s)):
	if s[i]=='z':
		x.append(s[i])
	else:
		y.append(s[i])
if (2 * len(x) == len(y)):
	print("Yes")
else:
	print("No")
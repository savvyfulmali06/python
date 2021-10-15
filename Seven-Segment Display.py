
## Print the largest possible number numerically that can be generated using at max that many number of matchsticks which was used to generate N.

d={0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}

T = int(input())

while T>0:
	num=input()
	sum=0
	for i in num:
		sum+=d[int(i)]
	if sum%2==0:
		print('1'*(sum//2))
	else:
		print((sum//2))
		print('7'*1+'1'*((sum//2)-1))		
	T-=1
T = int(input())

while T>0:
	c = list(map(int,input().split()))
	u=int(input()) ##No of users
	g=0
	p=0
	for i in range(u):
		n=input().split()
		g+=int(n[0])
		p+=int(n[1])
	print(min([g*c[0]+p*c[1],g*c[1]+p*c[0]]))
	T-=1
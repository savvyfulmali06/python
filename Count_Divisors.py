## Count divisors

n=list(map(int,input().split()))
i=n[0]
l=n[1]
k=n[2]
c=0
for j in range(i,l+1):
	if (j%k ==0 ):
		c+=1
print(c)
		
		
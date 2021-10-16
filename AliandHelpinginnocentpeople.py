t=input()
v=['A','E','I','O','U','Y']
d0=int(t[0])
d1=int(t[1])
s2=t[2]
d3=int(t[3])
d4=int(t[4])
d5=int(t[5])
d7=int(t[7])
d8=int(t[8])
if any(e in s2 for e in v):
	print("invalid")
elif (((d0+d1)%2==0) & ((d3+d4)%2==0) & ((d4+d5)%2==0) & ((d7+d8)%2==0)):
	print("valid")
else:
	print("invalid")
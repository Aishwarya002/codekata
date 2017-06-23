x=raw_input("enter a number")
z=len(x)
print(z)
y=int(x)
y1=int(x)
result=1
sum=0
while(y!=0):
	remin=y%10
	result=1
	for i in range(z):
		result=result*remin
	sum=sum+result
	y=y/10
if(sum==y1):
	print("amstrong")
else:
	print("not")

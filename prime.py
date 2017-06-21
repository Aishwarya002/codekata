count=0
x=input("enter a number")
for i in range(x,x/2):
	if(x%i==0):
		print("number is not prime")
		count=1
if(count==0):
	print("prime number")
else:
	print("not a prime")

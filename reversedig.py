x=input("enter a number")
sum=0
while(x!=0):
	remin=x%10
	sum=(sum*10)+remin
	x=x/10
print(sum)

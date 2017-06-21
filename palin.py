x=input("enter a number")
y=x
r=0
while(x!=0):
	re=x%10
	r=r*10+re
	x=x/10
print(r)
if(r==y):
	print("palindrome")
else:
	print("not a palindrome")

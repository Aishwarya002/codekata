x=input("enter a number")
y=x
result=0
while(y!=0):
	remin=y%10
	result=result+remin*remin*remin
	y=y/10
print(result)
if(result==x):
	print("amstrong")
else:
	print("not")

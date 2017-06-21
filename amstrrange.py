x=input("enter a number")
x1=input("enter another number")
y=x
result=0
for i in range(x,x1):
	result=0
	y1=i
	while(i!=0):
		remin=i%10
		result=result+remin*remin*remin
		i=i/10
	if(result==y1):
		print("amstrong")
		print(y1)

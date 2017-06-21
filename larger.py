x=input("enter a number1")
y=input("enter a number2")
z=input("enter a number3")
listt=[]
listt.append(x)
listt.append(y)
listt.append(z)
for i in range(0,3):
	for j in range(i+1,3):
		if(listt[i]>listt[j]):
			t=listt[i]
			listt[i]=listt[j]
			listt[j]=t
print(            listt[2])

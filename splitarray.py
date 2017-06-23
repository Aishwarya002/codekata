x=int(input("enter a number"))
y=int(input("enter a number"))
lst=[]
lst1=[]
for i in range(x):
	y1=int(input("enter a number"))
	lst.append(y1)
print(lst)
for i in range(y,x):
	lst1.append(lst[i])
for i in range(y):
	lst1.append(lst[i])
print(lst1)

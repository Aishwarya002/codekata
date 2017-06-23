x=int(input("enter a number"))
lst=[]
count=0
lstt=[]
for i in range(x):
	y=int(input("enter a number"))
	lst.append(y)
print(lst)
for i in range(x):
	count=0
	for j in range(x):
		if(lst[i]==lst[j]):
			count=count+1
	lstt.append(count)
leng=len(lstt)
for i in range(leng):
	if(lstt[i]==1):
		print(lst[i])

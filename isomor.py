x=raw_input("enter a string")
y=raw_input("enter another string")
x1=len(x)
y1=len(y)
listt=[]
count=0
if(x1==y1):
	print("true")
	for i in range(x1):
		listt.append(i)
		for j in range(1,x1): 
			if(x[i]==x[j]):
				listt.append(j)		
		leng=len(listt)
		for i in range(leng):
			for j in range(y1):
				if(y[i]==y[j]):
					count=count+1
		if(count==leng):
			print("true")
			listt.clear()
		else:
			print("false")
			

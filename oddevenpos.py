x=raw_input("enter a string")
y=len(x)
ar=[]
ar1=[]
final=[]
l3=0
print(y)
for i in range(y):
	if(i%2==0):
		ar.append(x[i])		
	else:
		ar1.append(x[i])
l1=len(ar)
l2=len(ar1)
if(l1>l2):
	l3=l1
else:
	l3=l2
for i in range(l3):
	final.append(ar1[i])
	final.append(ar[i])
print(''.join(final))


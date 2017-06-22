x=raw_input("enter a string")
y=x[::-1]
listt=[]
lst=[]
leng=len(y)
for i in range(leng):
	listt.append(y[i])
for i in range(leng):
	if(listt[i]=='a' or listt[i]=='e' or listt[i]=='i' or listt[i]=='o' or listt[i]=='u'):
		listt[i]=' '
lst=' '.join(listt).split()
print(lst)
print(''.join(lst))

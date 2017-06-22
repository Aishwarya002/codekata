x=raw_input("enter a day(all caps)")
def work(x):
	if(x=='MONDAY' or x=='TUESDAY' or x=='WEDNESDAY' or x=='THURSDAY' or x=='FRIDAY'):
		return 'true'
	else:
		return 'false'
y=work(x)
print(y)

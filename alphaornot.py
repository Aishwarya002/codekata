x=raw_input("enter a digit or a string")
if(x.isalpha()):
	print("string")
elif(x.isdigit()):
	print("digit")
else:
	print("alphanumeric")

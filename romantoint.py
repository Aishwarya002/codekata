x=raw_input("enter any roman numerals")
roman=['I','II','III','VI','V','VI','VII','VIII','IX','X']
val=['1','2','3','4','5','6','7','8','9','10']
y=len(roman)
for i in range(y):
	if(roman[i]==x):
		print(val[i])

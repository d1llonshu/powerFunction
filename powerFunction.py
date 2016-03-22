#Define the power function 
def power(base, exponent): 
	placeholder = 1
	newbase = base
	while placeholder < exponent:
		newbase = newbase * base
		placeholder = placeholder + 1
	
	if exponent == 0:
		return 1
	else:
		return newbase

#Number times Number exponent's amount of times 



base = input("Insert a number ")
exponent = input("Insert an exponent ")
base = int(base)
exponent = int(exponent)


print(power(base,exponent))
a = input("enter the string")
al=0
di=0
sp=0
for i in a:
	if i.isalpha():
		al=al+1
	elif i.isdigit():
		di=di+1
	else:
		sp=sp+1	
print("count of alphabet=",al,"count of digit=",di,"count of special charter=",sp)

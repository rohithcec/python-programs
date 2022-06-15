a = input("enter the string")
v= ['a','e','i','o','u']
print(type(v))
x=0
c=0
for i in a:
	if i in v:
		x=x+1
	else:
		c=c+1	
print("count of vowels=",x)
print("count of constants=",c)

a = input("enter the string")
v= ['a','e','i','o','u']
print(type(v))
for i in a:
	if i in v:
		x=(a.replace(i,'x'))
		
print(x)

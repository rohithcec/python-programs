a = input("enter the string")
for i in range(0,(len(a)-1)):
	for j in range(i,(len(a)-1)):
		if a[j]==a[i]:
			a=a.replace(a[i],'')
print(a)

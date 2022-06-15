f=open("num.txt","r")
num=f.read()
print(num)
su=0
for i in num:
	if i.isdigit() == True:
            sum = sum + int(i)
print(su)

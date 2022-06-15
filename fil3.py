f=open("num.txt","r")
num=f.read()
ls=[]
su=0
ls=num.split()
for i in range(0,len(ls)):
	su=su+int(ls[i])
print(su)
f.close()

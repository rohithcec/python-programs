import random
f=open("random.txt","w")
for i in range(1,101):
	m=random.randint(1,100)
	f.write(str(m)+'\n')
f.close()
f=open("random.txt","r")
n=f.read()
print(n)	
f.close()

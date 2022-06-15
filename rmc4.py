a = input("enter the string")
frq={}
for i in a:
	if i in frq:
		frq[i]=frq[i]+1
	else:
		frq[i]=1	
res=max(frq,key=frq.get)
print("highest freqency character=",res)

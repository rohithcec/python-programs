a=[[1,2],[3,4],[5,6]]
b=[[1,2],[3,4],[5,6]]
c=[[0,0],[0,0],[0,0]]
for i in range(len(a)):
	for j in range(len(a[0])):
		c[i][j]=a[i][j] + b[i][j]
print(c)

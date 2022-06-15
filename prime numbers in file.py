f=open("prime.txt","w")
n=int(input("enter the limit"))
for number in range (2, n):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            f.write(str(number)+'\n')
           
f.close()


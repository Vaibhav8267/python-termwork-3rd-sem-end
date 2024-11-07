n=int(input("Size of series: "))
sum=0.0
fact=1
for i in range(n):
    fact=fact*(i+1)
    sum+=1/fact
print(sum)
    
    
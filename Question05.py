def fibo(n):
    if n==1 or n==0:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
size=int(input("Enter size of series: "))
for i in range(size):
    print(fibo(i),end=" ")
def checkpalindrome(num):
    return(str(num) == str(num)[::-1])
def print_num(replica):    
    if(checkpalindrome(replica)):
     print(replica,end=" ")
for i in range(1,100):
    print_num(i)
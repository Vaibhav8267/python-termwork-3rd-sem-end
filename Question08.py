file=open("Grade.text","r")
avg=0.0
sum=0
count=0
for i in file:
    count+=1
    sum+=int(i)
avg=sum/count
print(f"Total marks of {count} subjectes are: {sum}")
print (f"Percentage is: {avg}% ")       
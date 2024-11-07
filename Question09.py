file1=open("demo.txt","r")
file2=open("Demo_output.txt","w")
for i in file1:
    if i and i[0].isupper():
        file2.write(i)


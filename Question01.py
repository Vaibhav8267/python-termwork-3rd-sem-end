str=input("Enter a String: ")
x=str.strip()
print(f"{str} is Striped to ",x)
print(f"{x} is Capitalize to ",x.capitalize())
print(f"{x} is Lowered to ",x.lower())
print(f"{x} is Uppered to ",x.upper())
print(f"{x} length is:  ",len(x))
set1={1,2,3,4,5,6}
set2={1,2,3,4,8,9,11,12}
print("Union= ",set1.union(set2))
print("intersection= ",set1.union(set2))
print("largest number: ",max(set2)); 
set1.discard(1)
print("Remove  1 from set1: ",set1)
set1.clear()
print("clear set:  ",set1)

tup=(1,2,2,3,4,5,6,1,7)
print("Length: ",len(tup))
print("Maximum number: ",max(tup))
print("Minimum number: ",min(tup))
print("Number of 1 in tuples: ",tup.count(1))
print("Sorted tuple: ",sorted(tup))


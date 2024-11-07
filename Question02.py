dict = {}
def add_students(): 

    n = int(input("Number of Students: "))
    for i in range(n):
        key = input(f"Enter key {i + 1}: ")
        x=int(input("Enter number of subjects: ")) 
        marks=[]
        for j in range(x):
            value = input(f"Enter subject marks for '{key}': ")
            marks.append(value) 
            dict[key]=marks
def update_marks():
    name = input("Enter the student name to update marks: ")
    if name in dict:
        new_marks = []
        num_subjects = int(input(f"Enter the new number of subjects for {name}: "))
        for i in range(num_subjects):
            mark = int(input(f"Enter new mark for subject {i + 1}: "))
            new_marks.append(mark)
        dict[name] = new_marks
        print(f"Marks for {name} have been updated.\n")
    else:
        print("Student not found.\n")
def remove_stud():
    name = input("Enter the student name to remove: ")
    if name in dict:
        del dict[name]
    else:
        print("Student not found.\n")
def highest():
   name=input("Enter name of student: ")
   if name in dict:
       x=max(dict[name])
       print(f"{name} Highest marks is {x}")
def avg():
    if not dict:
        print("No students found.")
    else:
        for name, marks in dict.items():
            average = sum(marks) / len(marks)
            print(f"Student: {name}, Average Marks: {average:.2f}")
    print()
add_students()
update_marks()
remove_stud()
avg()
highest()
n=int(input("Enter Number of students : "))
print("      Enter Subject Name")
s=[1,2,3,4]
x=0;
for i in range(4):
    print("Subject-",i+1," : ",end='')
    s1=str(input())
    s[i]=s1

student={}

for i in range(n):
    d={}
    print("    ",i+1,"- Name of student : ",end='')
    x=str(input())
    print("Enter marks of ",x)
    for j in range(4):
        print("marks of - ",s[j]," : ",end='')
        m=int(input(""))
        d[s[j]]=m

    student[x]=d
    print()
          
print("\n\nEnter The name of the students and subject to check ")
name=str(input("Name : "))
subject=str(input("Subject : "))
print("Marks : ",end='')
print(student[name][subject])

print(student[name][subject])

def highest_marks(s):
    x=0
    name=""
    for i in s:
        y=x
        x=0
        for j in i:
            x+=s[i][j]
        if(x>y):
            name=i
        else:
            x=y

    print("\n\n\n",name)
    
#highest_marks(student)

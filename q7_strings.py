def find_length(s):
    x=0
    for i in s:
        x+=1
    return x
 
def replace_vowels(s):
    for i in s:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A'or i=='E'or i=='I'or i=='O'or i=='U'):
            s=s.replace(i,"#")
    print(s)

def find_words(s):
    x=1
    for i in s:
        if(i==" "):
            x+=1
    print(x,"-Words in the string")

def palindrome(s):
    x=find_length(s)
    j=-1
    key=1
    for i in range(x):
        if(s[i]!=s[j]):
            print("Not-Palindrome")
            key=0
            break
        j-=1
    if(key):
        print("Palindrome")

def greater_string(s1,s2,s3):
    x=len(s1)
    y=len(s2)
    z=len(s3)
    s=s1;
    if(x==z==y):
        for i in range(x):
            if(s1[i]==s2[i]==s3[i]):
                continue
            if(s1[i]>s2[i]):
                if(s1[i]>s3[i]):
                    s=s1
                else:
                    s=s3
            else:
                if(s2[i]>s3[i]):
                    s=s2
                else:
                    s=s3
        
    else:
        if(x>y):
            if(x>z):
                s=s1
            else:
                s=s3
        else:
            if(y>z):
                s=s2
            else:
                s=s3
                
    return s




s1=str(input("Enter first String : "))
key=1
while(key):
    print("\n\n      #########--MENU--#########")
    print("1.Find length of the String")
    print("2.Replace Vowels from the String")
    print("3.Find number of words in the String")
    print("4.check String is palindrome or not")
    print("5.check which String is maximum")
    print("6.EXIT")
    n=int(input("Enter Your choice : "))
    if(n==1):
        print("Lenght of the string : ",find_length(s1))
    elif(n==2):
        replace_vowels(s1)
    elif(n==3):
        find_words(s1)
    elif(n==4):
        palindrome(s1)
    elif(n==5):
        s2=str(input("Enter second string : "))
        s3=str(input("Enter third string : "))
        
        print("String-1 : ",s1)
        print("String-2 : ",s2)
        print("String-3 : ",s3)
        print("Maximum String : ",greater_string(s1,s2,s3))
    elif(n==6):
        key=0
    else:
        print("invalid Choice")
        print("do you want to continue or exit ")
        n=int(input("Enter 1 to continue : "))
        if(n!=1):
            key=0
            continue
        
    


def isallnumber(l1):
    for i in l1:
        if(isinstance(i,int)):
            continue
        else:
            return False
        
    return True

def count_odd(l1):
    if(isallnumber(l1)):
        x=0
        for i in l1:
            if(i%2!=0):
                x+=1
        print("Number odd Value : ",x)
    else:
        print("List is not numeric only")

def isallstring(l1):
    for i in l1:
        if(isinstance(i,str)):
            continue
        else:
            return False
        
    return True

def largest_string(l1):
    if(isallstring(l1)):
        x=""
        for i in range(len(l1)-1):
            if(l1[i]>l1[i+1]):
                x=l1[i]
            else:
                x=l1[i+1]
        return x
    return ""

def reverse(l1):
    x=-1
    for i in range(len(l1)):
        print(l1[x]," ",end='')
        x=x-1
    print()

def find(x,l1):
    for i in range(len(l1)):
        if(l1[i]==x):
            print(x," is at possition ",i)
            return


def sorting(l1):
    for i in range(len(l1)):
        x=l1[i]
        for j in range(i+1,len(l1)):
            y=l1[j]
            if(y>x):
                l1[j]=x
                x=y
                l1[i]=x
    print(l1)

def common(l1,l2):
    for i in l1:
        for j in l2:
            if(i==j):
                print(i," ",end='')
                break



l1=[34,3,5,6,7,34,7,5]
l2=[4,6,3,25,3,3,5,345,5]



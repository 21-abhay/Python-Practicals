def print_even(t1):
    print("Even value only : ",end='')
    for i in t1:
        if(i%2==0):
            print(i," ",end='')
    print()

def concatination(t1,t2):
    t1=t1+t2
    print("After cancatination : ",t1)

def maximum_value(t1):
    x=t1[0]
    for i in t1:
        if(i>x):
            x=i
    print("Maximum value in the tuple : ",x)

def minimum_value(t1):
    y=t1[0]
    for i in t1:
        if(i<y):
            y=i
    print("Minimum value in the tuple : ",y)

t1=(1,2,5,7,9,2,4,6,8,10)
t2=(11,3,0,14)

print_even(t1)
concatination(t1,t2)
minimum_value(t1)
maximum_value(t1)

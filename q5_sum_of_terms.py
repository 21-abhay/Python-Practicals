def fact(n):
    f=1
    for i in range(n):
        f*=i+1

    return f

def sum():
    n=int(input("Enter number of term : "))
    y=int(input("Enter The number : "))
    x=1
    i=2
    for j in range(n-1):
        if(i%4==0):
            x+=(y**i)/fact(i)
        else:
            x-=(y**i)/fact(i)
        i+=2

    print(" sum : ",x)

sum()

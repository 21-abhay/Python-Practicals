def fact(n):
    pro=1
    for i in range(1,n+1):
        pro=pro*i
    print("The factorial of ",n," is : ",end="")
    print(pro)

def fibo(n):
    a=0
    b=1
    print("Fibonacci series upto ",n,"-terms : ",end='')
    print(a," ",end='')
    print(b," ",end='')
    for i in range(n-2):
        c=a+b
        a=b
        b=c
        print(c," ",end='')

n=int(input("Enter the number  :"))
fact(n)
fibo(n)

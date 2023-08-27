
s1=40000
s2=50000
s3=60000
s4=80000
c=5/100

def commission(x):
    if(x<s2):
        return 0

    return c*x

def remarks(x):
    if(x<s1):
        print("\nRemark : WORK HARD\n")
    elif(x>=s1 and x<s3):
        print("\nRemark : AVERAGE SALEs\n")
    elif(x>=s3 and x<s4):
        print("\nRemark : GOOD SALEs\n")
    else:
        print("\nRemark : EXCELLENT SALEs\n")


print("Enter SAles of ")
w1=int(input("Week-1 : "))
w2=int(input("Week-2 : "))
w3=int(input("Week-3 : "))
w4=int(input("Week-4 : "))

total_sales=w1+w1+w3+w4
print("Total Sales of the month : ",total_sales)
com=commission(total_sales)

print("\n\nCommission = ",com)

remarks(total_sales)



s=str(input("Enter a sentence : "))
d={}
for i in s:
    if(i in d.keys()):
        d[i]+=1
        continue
    d[i]=1

print(d)
    

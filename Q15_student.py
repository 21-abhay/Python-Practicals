
class student:

    max_Avg=0
    

    def __init__(self,name,sub1,sub2,sub3):
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
        self.name=name
        self.marks=[self.sub1,self.sub2,self.sub3]

        avg = self.getAvg()
        
        if(avg > student.max_Avg ):
            student.max_Avg = avg

    def getAvg(self):
        
        return (self.sub1 + self.sub2 + self.sub3)/3
        

    def __del__(self):
        prit("destructor call")



a=student("abhay",78,98,98)
print("Avg = ",a.getAvg())
print("Max Avg = ",a.max_Avg)
b=student("arpit",87,78,97)
print("Avg = ",b.getAvg())
print("Max Avg = ",b.max_Avg)






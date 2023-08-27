import math


class triangle:

    def __init__(self,s1,s2,s3):
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.checking()
        print("Triangle is valid")

    def checking(self):
        assert self.s1<(self.s2+self.s3)
        assert self.s2<(self.s1+self.s3)
        assert self.s3<(self.s2+self.s1)

    def get_perimeter(self):
        return (self.s1+self.s2+self.s3)

    def get_area(self):
        s=self.get_perimeter()/2
        x=s-self.s1
        y=s-self.s2
        z=s-self.s3
        a=s*x*y*z
        
        area=math.sqrt(a)
        
        return area


side1=int(input("Enter length of side1 : "))
side2=int(input("Enter length of side2 : "))
side3=int(input("Enter length of side3 : "))


t=triangle(side1,side2,side3)
print("Perimeter = ",t.get_perimeter())
print("Area = ",t.get_area())

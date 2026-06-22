
class Rectangle:
    def __init__(self,length=0,width=0):
        self.length = length
        self.width = width        
        
    def Area(self):
        print(f"The area of the rectangle is : {self.length*self.width}")
        
    def Perimeter(self):
        print(f"The perimeter of the rectangle is : {2*(self.length+self.width)}")


def main():
   r = Rectangle(4,5)
   r.Area()
   r.Perimeter()
    
   pass
    
if(__name__ == "__main__"):
    main()
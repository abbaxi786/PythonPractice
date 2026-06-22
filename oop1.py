
class Students:
    
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
        pass
    
    def IsPass(self):
        if(self.marks>49):
            print(f"The student named {self.name} is passed")
        else:
            print(f"The student named {self.name} is failed")
            

def main():
    s1 = Students("Faraz", 15,45)
    s2 = Students("Faiz", 15, 70)
    s1.IsPass()
    s2.IsPass()
    
if(__name__ == "__main__"):
    main()


class Students:
    
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
        pass
    
    def __str__(self):
        return f"{self.name} of {self.age} age has {self.marks} marks"
        pass
    
    
            

def main():
    s1 = Students("Farhan", 19,87);
    print(s1)    
    pass
    
if(__name__ == "__main__"):
    main()



class Animal:
    def Sound(self):
        print("Make sound")
        
class Dog(Animal):
    def Sound(self):
        print("Bark")
        
class Cat(Animal):
    def Sound(self):
        print("Meow")
        
def main():
    a = Animal()
    d = Dog()
    c = Cat()
    
    a.Sound()
    d.Sound()
    c.Sound()
    
if(__name__ == "__main__"):
    main()
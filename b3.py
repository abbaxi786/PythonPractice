

def Add(x,y):
    return x+y

def Mul(x,y):
    return x*y
def Sub(x,y):
    return x-y
def Div(x,y):
    if(y==0):
        print("Can't divisible with zero")
        return 
    return x/y

print(f"2+6 {Add(2,6)}")
print(f"2*6 {Mul(2,6)}")
print(f"6-2 {Sub(6,2)}")
print(f"6/2 {Div(6,2)}")
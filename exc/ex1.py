
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    try:
        return x / y
    except ZeroDivisionError as e:
        print(str(e))
        return None
    
div(1,0)
            

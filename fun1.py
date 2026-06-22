
def Prime(number):
    if(number<=1):
        return False
    elif(number== 2):
        return True
    elif(number%2 == 0):
        return False
    else:
        for i in range(3,number):
            if(number%i== 0):
                return False
    
    return True
       
        
print(f"This is {"a" if Prime(23) else "not"} prime number")
# FizzBuzz: 1 to 50 — "Fizz" for multiples of 3, "Buzz" for 5, "FizzBuzz" for both. 

prompt = int(input("Enter the value btw 1 and 50:  "))

def FuzzAndBuss(value):
    M_of3AndM_of5 = (value % 3 == 0 and value % 5 == 0)
    M_of3 = (value % 3 == 0)
    M_of5 = (value % 5 == 0)
    out_of_range = (value < 1 or value > 50)
    if(out_of_range): 
        print("Out of range") 
        return    
    if(M_of3AndM_of5): print("FizzBuzz")
    elif(M_of3): print("fizz")
    elif(M_of5): print("Buzz")
    else: print("Not fizz and buzz")
    


FuzzAndBuss(prompt)
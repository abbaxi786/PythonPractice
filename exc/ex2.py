

while True:
    try:                
        value = int(input("Enter the number"))
        break
    except ValueError as e : 
        print("Enter the number not the characters")
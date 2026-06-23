

age = int(input("Enter the age: "))
if(age<0):
    raise ValueError("The age should be positive")
print(f"The age is {age}")
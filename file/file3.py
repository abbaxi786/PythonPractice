
name = input("Enter your name: ")
phoneNo = input("Enter your number: ")

with open("file.txt",'a') as file:
    file.write(f"{name} [{phoneNo}]\n")
    

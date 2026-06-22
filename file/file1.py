

with open("file.txt","w") as file:
    file.write("Hello this is my file")
    
with open("file.txt","r") as file:
    txt = file.read()
    
    print(txt)
    


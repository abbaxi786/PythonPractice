

with open("file.txt","r") as file:
    
        content = file.read();
        
        lines = content.split("\n")
        totalWords =0
        for i in lines:
         value = i.split()
         if(value):
            totalWords+= len(value)
        
        print(f"The total number of words in it is : {totalWords}")
        print(f"The total number of lines in it is : {len(lines)}")
        
        

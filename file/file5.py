

search = input("Enter the searched word:  ")
numberOfOccurance =0
lineNo =[]
number =0


with open("file.txt","r") as file:
    
        content = file.read();
        
        lines = content.split("\n")
        totalWords =0
        for i in lines:
            words = i.split()
            number += 1
            for word in words:    
                if(search.lower()==word.lower()):
                    numberOfOccurance+=1
                    lineNo.append(number)
            
             
        print(f"The number of occurance of word is {numberOfOccurance} and are those line number: {lineNo}")
         
        
        
        
        

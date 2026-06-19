# guess-the-number game: the program picks a number, the user keeps guessing

start = 0
correctGuessed = 12

def GuessValue():
    while True:
        value = int(input("Guess the number:"))
        if(value== correctGuessed): 
            print("Correct Guess\n")
            break
        elif(value > correctGuessed): print("Lot higher\n")
        elif(value < correctGuessed): print("Lot lower\n")
        

GuessValue()
        
         


def Vowel(word):
    vowelSum = 0
    for i in word:
        if(i == 'a' or i == "e" or i == "i" or i == "o" or i == 'u'):
            vowelSum += 1
    
    return vowelSum
        
        
print(Vowel("How are you"))
    
# Store 5 friends' names in a list, then print them all in uppercase. 

friends = ["Ali", "Afzal", "Ahmad", "Fazal", "Faisal"]

for i in range(len(friends)):
    friends[i] = friends[i].upper()
    
print(friends)
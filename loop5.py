# Use a list comprehension to get the square of every number from 1 to 10 in one line. 

arr = []

for i in range(1,11):
    arr.append(i)
    
squares = [i*i for i in arr]

print(squares)
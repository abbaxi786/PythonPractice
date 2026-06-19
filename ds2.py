# Find the largest and smallest number in a list — first with max()/min(), then without them

numbers = [2,6,8,9,4,6]

print(f"The max values among the numbers is: {max(numbers)}")
print(f"The minimum values among the numbers is: {min(numbers)}")

maxValue = numbers[0]
for item in numbers:
    if(maxValue<item): maxValue = item
    
print("Max value with max func: ",maxValue)

minValue = numbers[0]
for item in numbers:
    if(maxValue>item): maxValue = item
    
print("Min value with min func: ",minValue)

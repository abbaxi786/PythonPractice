
def SumAndAverage(lists):
    sum = 0
    for i in lists:
            sum += i
    
    print(f"The sum of List is : {sum}")
    print(f"The average of list is : {int(sum/len(lists))}" )
    
    
SumAndAverage([2,6,6,6,5,4,5])
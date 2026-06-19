# Build a dictionary of student names and marks, then calculate the average. 

dic = [
    {
        "name" : "Fazal",
        "marks": 56
    },
    {
        "name" : "Bassam",
        "marks": 70
    },
    {
        "name" : "Bashir",
        "marks": 55    },
    {
        "name" : "Farhan",
        "marks": 83
    }
]
sum = 0
for item in dic:
    sum+= item["marks"]
    
avg = sum /len(dic)

print(f"Average of number: {avg}")

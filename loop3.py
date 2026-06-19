# Print the multiplication table of a given number. 

table = int(input("Enter the table number: "))

def PrintTable(tableNo):
    print(f"\n\nTable of {tableNo}\n")
    for i in range(1,11):
        print(f"{tableNo} X {i} = {tableNo * i}\n")
    
PrintTable(table)
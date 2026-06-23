
try:
    with open('file.txt','r') as file:
        content =file.read()
        print(content)
except FileNotFoundError as e:
    print("File not exist")
except Exception as e:
    print(str(e))
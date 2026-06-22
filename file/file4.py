import json

dicts = {
    "name": "Bassam",
    "age": 21,
    "marks": 80
}

with open('file.json','w') as file:
    json.dump(dicts,file)
    
with open("file.json","r") as file:
    data = json.load(file)
    print(data)    
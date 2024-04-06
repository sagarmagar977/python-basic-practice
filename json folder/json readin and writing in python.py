import json
file=open("sample1.json","r")
x=file.read()
finaldata=json.loads(x)
print(x) 
for a in finaldata:
    print(a) 
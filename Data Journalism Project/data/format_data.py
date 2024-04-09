import json

f1 = open("number of returns per group.csv", "r")
lines = f1.readlines()
    
   
dictionary = {}
    
    
    for row in lines:
        for bracket, value in row.items():
            if bracket != 'Year':
                if bracket not in dictionary:
                    dictionary[bracket] = {}
                dictionary[bracket][row['Year']] = value
f1.close()

f2 = open("number of returns per group.json", "w"):
json.dump(dictionary, f2, indent=4)

f2.close()

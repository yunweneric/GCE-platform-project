#SAMPLE CENTER NUMBER STRUCTURE
results = {
    "info": {
        "Center number": 11001,
        "Regist": 167,
        "Sat for 2 or more Subjects": 149,
        "Passed": 75,
        "% Passed": 50.34,
        "Sanctioned": 4,
    },
    "Passed In 5 Subjects":{
        "NAME" : "RESULT",
        "NAME1": "Result",
        "NAME2": "Result",
        "NAME3": "Result",
    },
    result {
        stud
        {
            
        }
    }
    "Passed In 4 Subjects":{
        "NAME" : "RESULT",
        "NAME1": "Result",
        "NAME2": "Result",
        "NAME3": "Result",
    },
    "Passed In 3 Subjects":{
        "NAME" : "RESULT",
        "NAME1": "Result",
        "NAME2": "Result",
        "NAME3": "Result",
    },
    "Passed In 2 Subjects":{
        "NAME" : "RESULT",
        "NAME1": "Result",
        "NAME2": "Result",
        "NAME3": "Result",
    },        
}

#Stringifying the dictionary
stringified = str(results)
print(type(stringified))

#Accessing the dictionary
print(results)

#Acessing info
print(results["info"])

#Accessing Results
print(results["Passed In 5 Subjects"])

#Accessing the student's result
print(results["Passed In 5 Subjects"]["NAME"])

#Converting the sringified dictionary to an actual dictionary
# import json
# data = json.loads(stringified)
# print(type(data))
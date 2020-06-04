
# #relacing the info object
# import re
# string = "444R 703SOKAMTE 333HO"

# data1 = re.findall(r"\d+[A-Z]", string)
# print(data1)
# for i in data1:
#     data = re.findall(r"\d+", i)
#     # print(data1)




#     # print(i)
# # for i in data:
#     # data = re.split(r"", string,)
#     # print(data)
#     # if type(type(data[0]) == int):
#     #     print("string")
#     # else:
#     #     pass




# # print(data)
# # print(type(data[3]))
# # if type(type(data[3]) == int):
# #     print("hh")
# # else:
# #     pass


# # print(type(True))

#================================================
# import re
# string = "10.DISSOK TIOMELA LESLY BIO-B,PHY-E 11.249of19Page"

# string = "4.249of1Page"

# # regex = re.findall("^\d+\.\d+\w+", string)
# regex = re.sub("^\d+\.\d+\w+", "yes", string)
# print(regex)

# import re

# import json
# raw = {
#     "info": {
#         "Center number": 11001,
#         "Regist": 167,
#         "Sat for 2 or more Subjects": 149,
#         "Passed": 75,
#         "% Passed": 50.34,
#         "Sanctioned": 4,
#     },
#     "Passed In 5 Subjects":{
#         "NAME : RESULT",
#         "NAME1","Result",
#         "NAME2","Result",
#         "NAME3","Result",
#     },
#     "Passed In 4 Subjects":{
#         "NAME1","Result", "grade",
#         "NAME2","Result", "grade",
#         "NAME3","Result", "grade",
#     }
#     "Passed In 3 Subjects" = {
#         "NAME1","Result", "grade",
#         "NAME2","Result", "grade",
#         "NAME3","Result", "grade",
#     }
#     "Passed In 2 Subjects" = {
#         "NAME1","Result", "grade",
#         "NAME2","Result", "grade",
#         "NAME3","Result", "grade",}
# }
# raw = str(raw)
# print(raw)
# finale = json.loads(raw)
# print(type(finale))

# import re

# txt = "The rain in Spain and after the following, there is (7) another The Spain What wrong (8) what abou the rest (9)"
# x = re.search(r"(Spain and).*?\(", txt)

# print(x)
# # if type(x) == 'None':
# print(x.group(0))
#=====================================================================================================



import re
list = "21 noella2 3 4 5jesus 655555 , 7 great"
list2 = ["1","22","3","4","5","6","7"]


res = re.findall("\d+\w+", list)

print(res)
print(type(res))


strin = "MAKOKI COLETTE ECO-C,LIT-E,HIS-D (1)FOINTAMA MELISA BI BIO-B,CHE-E,PHY-E (2)AKAM PRINCELY MBAH ECO-E,GEO-E,HIS-C (3)ALIYOU AYUBA BIO-E,CHE-D,PHY-E (4)NDEM RANDY ANCHOUR ECO-E,GEO-E,HIS-E (5) TANYI VILEROY EJANG ECO-A,GEO-C (1)NYUKA YANGO BARBARA HIS-C,PHI-D (2)MBACHAM COLLINS MBACHAM ECO-D,HIS-E (3)WILBA HERMANN ANGELOS ECO-D,GEO-E (4)DJINDA KAMGANG WILLIAM TYCHIQUE BIO-E,CHE-E (5)KALA KENMOE DIDINE ZITA ECO-E,HIS-E (6)"

fin = re.findall("([A-Z]-?'?)+ .*?\(", strin)
print(fin)


print("#".join(list2))










#([A-Z]-?'?)+ .*?\(


# "Centre No": 12352 Douala Iii External  
# Regist: 15, 
# Sat for 2 or more Subjects:  15,
# Passed: 11
# %Passed: 73.33, 
# Sanction: 0 

# MAKOKI COLETTE ECO-C,LIT-E,HIS-D (1)FOINTAMA MELISA BI BIO-B,CHE-E,PHY-E (2)AKAM PRINCELY MBAH ECO-E,GEO-E,HIS-C (3)ALIYOU AYUBA BIO-E,CHE-D,PHY-E (4)NDEM RANDY ANCHOUR ECO-E,GEO-E,HIS-E (5) 

# TANYI VILEROY EJANG ECO-A,GEO-C (1)NYUKA YANGO BARBARA HIS-C,PHI-D (2)MBACHAM COLLINS MBACHAM ECO-D,HIS-E (3)WILBA HERMANN ANGELOS ECO-D,GEO-E (4)DJINDA KAMGANG WILLIAM TYCHIQUE BIO-E,CHE-E (5)KALA KENMOE DIDINE ZITA ECO-E,HIS-E (6)



# "Centre No": 12353 Tombuka External  
# Regist: 47, 
# Sat for 2 or more Subjects:  45,
# Passed: 33
# %Passed: 73.33, 
# Sanction: 0 



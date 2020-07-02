# import re

# txt = "The rain in Spain and after the following, there is (7) another The Spain What wrong (8) what abou the rest (9)"
# x = re.search(r"(Spain and).*?\(", txt)

# print(x)
# # if type(x) == 'None':
# print(x.group(0))
#=====================================================================================================



# import re
# list = "21 noella2 3 4 5jesus 655555 , 7 great"
# list2 = ["1","22","3","4","5","6","7"]


# res = re.findall(r"\d+\w+", list)

# print(res)
# print(type(res))


# strin = "MAKOKI COLETTE ECO-C,LIT-E,HIS-D (1)FOINTAMA MELISA BI BIO-B,CHE-E,PHY-E (2)AKAM PRINCELY MBAH ECO-E,GEO-E,HIS-C (3)ALIYOU AYUBA BIO-E,CHE-D,PHY-E (4)NDEM RANDY ANCHOUR ECO-E,GEO-E,HIS-E (5) TANYI VILEROY EJANG ECO-A,GEO-C (1)NYUKA YANGO BARBARA HIS-C,PHI-D (2)MBACHAM COLLINS MBACHAM ECO-D,HIS-E (3)WILBA HERMANN ANGELOS ECO-D,GEO-E (4)DJINDA KAMGANG WILLIAM TYCHIQUE BIO-E,CHE-E (5)KALA KENMOE DIDINE ZITA ECO-E,HIS-E (6)"

# # fin = re.findall(r"{([A-Z]-?'?)+\s?([A-Z]-?'?)+\s?(([A-Z]-?'?)+)?\s?(([A-Z]-?'?)+)?\s?([A-Z]+-[A-E],?)+}", strin)
# fin = re.findall(r"(([A-Z]-?'?)+ .*?\()", strin)


# print(fin)


# print("#".join(list2))

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


# list1 = ["('TEBOH CALISIUS TEKOH CHE-E,PHY-D (', 'H')", "('EWANOGE CLARA SENGE ECO-E,HIS-D (', 'E'),"]
# # list1 = list(filter(lambda x:x[1:-9] , list1))
# # print(list1)
# # list = "('TEWANG GERALD TEMBENG GEO-E,HIS-E (', 'G')"

# print(list[2:-9])

# for i in list1:
#     i = i[2:-9]
#     print(i)
    # else:
# ===============================================================================================================================



# list = ['NJONG MARTIN GIANG ECO-C,HIS-C,PHI-B', 'ETONGWE GRACE ESAKE ENG-B,LIT-C,HIS-C', 'NGONG YVETTE BINENG BIO-B,CHE-E,FSN-B', 'JU VAMAL MBONG ECO-A,GEO-C,PMS-E','GRACE-KELLY ENANGA FENDE ECO-E,GEO-E,HIS-D', "NDUMBI SHALOM MANKA'A BIO-D,PMS-C"]

# import json
# list = json.dumps(list)
# print(list)
# # for i in list:
#     # print(i)

# ================================================================================================================================

list = ["NSOH AKAME SHARON LIT-E,HIS-D,PHI-E", "NJINUWOH ANTHIONE TASSAH LIT-E,HIS-C", "NFORMI SHEKINAH-GLORY YULA ENG-C,LIT-E", "AKWO NGWA BEATRICE ECO-E,GEO-E", "MBUI ZEPHANIAH ASELIKWE ECO-E,GEO-E", "EKUKA CYNTHIA KIRA ECO-D,GEO-D,HIS-E", "CHIANKEM LAURENTINE CHIAFIE TENGIM BIO-B,CHE-D,PMM-E,PHY-D,ICT-C", "MUATEH YEYE GLORY ENG-D,LIT-E,HIS-B,PHI-A", "MISSI CYNTHIA PENGHA ECO-C,LIT-E,HIS-B,PHI-D", "GLORY MBUDZI ECO-A,ENG-E,GEO-E,HIS-C", "WIRBA RASMIRATU DZELAMONYUY ECO-B,ENG-D,GEO-E,HIS-C","NDUMBI SHALOM MANKA'A BIO-D,PMS-C"]



for i in list:
    print(i)
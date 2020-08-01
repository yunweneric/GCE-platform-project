#=======================================================================================================================                  
# # 1: Importing dependecies
import PyPDF4
import re

# ======================================================================================================================
                                    # O LEVELS
# ======================================================================================================================
def Get_Oldata(gce):
    # 2: Reading pdf #1.3. splice out name and store in a variable
    Files = open(gce, 'rb')

    # Initialize the Raw data container
    Raw_data = ""

    # 3: Loading files
    Loaded_pdf = PyPDF4.PdfFileReader(Files)

    # 4: saving content to a string called content
    content = Loaded_pdf.numPages
    f = open("Olgen.txt", "w")
    # 4.1: looping through all pages to access modify content
    for i in range(content):
        # 4.2: Reading(looping through all pages)
        page = Loaded_pdf.getPage(i)

        #1.3. splice out name and store in a variable
        # 4.3: Extracting raw data
        Raw_data = Raw_data + " " + page.extractText()
        # 4.4: Replacing bannar
    Data = Raw_data.replace("2019 RESULTS: GCE ADVANCED LEVEL GENERAL", "")
    Data = Data.replace("2019 RESULTS: GCE ORDINARY LEVEL GENERAL", "")
    Data = Data.replace("2019 RESULTS: GCE ORDINARY LEVEL TECHNICAL", "")
    Data = Data.replace("2019 RESULTS: GCE ADVANCED LEVEL TECHNICAL", "")
    # Reorganising work using Using regex and string methods
    import re
    Data = Data.replace("\n", "")
    Data = re.sub(r"\d+.\d+of\d+\w+", "", Data)
    # Data = re.sub(r"\(\d+\)", "", Data)
    Data = re.sub(r"Passed In \d+ Subjects: \d+", "", Data)
    Data = re.sub(r"Passed In \d+ Subjects:\d+", "", Data)
    Data = re.sub(r"\( In \d+ Subjects: \d+", "", Data)
    # Data = Data.replace("(", "")


    # USE REGEX TO MODIFY THE STUDENT'S RESULTS. EX. HIS-BNAME ===> HIS-B NAME............

    Data = Data.replace("HIS-A", "HIS-A ")
    Data = Data.replace("HIS-B", "HIS-B ")
    Data = Data.replace("HIS-C", "HIS-C ")

    Data = Data.replace("GEO-A", "GEO-A ")
    Data = Data.replace("GEO-B", "GEO-B ")
    Data = Data.replace("GEO-C", "GEO-C ")

    Data = Data.replace("MAT-A", "MAT-A ")
    Data = Data.replace("MAT-B", "MAT-B ")
    Data = Data.replace("MAT-C", "MAT-C ")

    Data = Data.replace("CHE-A", "CHE-A ")
    Data = Data.replace("CHE-B", "CHE-B ")
    Data = Data.replace("CHE-C", "CHE-C ")

    Data = Data.replace("BIO-A", "BIO-A ")
    Data = Data.replace("BIO-B", "BIO-B ")
    Data = Data.replace("BIO-C", "BIO-C ")


    Data = Data.replace("ECO-A", "ECO-A ")
    Data = Data.replace("ECO-B", "ECO-B ")
    Data = Data.replace("ECO-C", "ECO-C ")

    Data = Data.replace("PHY-A", "PHY-A ")
    Data = Data.replace("PHY-B", "PHY-B ")
    Data = Data.replace("PHY-C", "PHY-C ")

    Data = Data.replace("REL-A", "REL-A ")
    Data = Data.replace("REL-B", "REL-B ")
    Data = Data.replace("REL-C", "REL-C ")

    Data = Data.replace("LOG-A", "LOG-A ")
    Data = Data.replace("LOG-B", "LOG-B ")
    Data = Data.replace("LOG-C", "LOG-C ")


    Data = Data.replace("COM-A", "COM-A ")
    Data = Data.replace("COM-B", "COM-B ")
    Data = Data.replace("COM-C", "COM-C ")

    Data = Data.replace("LIT-A", "LIT-A ")
    Data = Data.replace("LIT-B", "LIT-B ")
    Data = Data.replace("LIT-C", "LIT-C ")


    Data = Data.replace("HBI-A", "HBI-A ")
    Data = Data.replace("HBI-B", "HBI-B ")
    Data = Data.replace("HBI-C", "HBI-C ")


    Data = Data.replace("CZE-A", "CZE-A ")
    Data = Data.replace("CZE-B", "CZE-B ")
    Data = Data.replace("CZE-C", "CZE-C ")

    Data = Data.replace("ENG-A", "ENG-A ")
    Data = Data.replace("ENG-B", "ENG-B ")
    Data = Data.replace("ENG-C", "ENG-C ")

    Data = Data.replace("FRE-A", "FRE-A ")
    Data = Data.replace("FRE-B", "FRE-B ")
    Data = Data.replace("FRE-C", "FRE-C ")

    Data = Data.replace("AMA-A", "AMA-A ")
    Data = Data.replace("AMA-B", "AMA-B ")
    Data = Data.replace("AMA-C", "AMA-C ")

    Data = Data.replace("SBEF-A","SBEF-A ")
    Data = Data.replace("SBEF-B","SBEF-B ")
    Data = Data.replace("SBEF-C","SBEF-C ")


    Data = re.sub(r"Sanctioned : \d+", "\n", Data)
    Data = Data.replace("Centre No:  ", '\n\n\n\n"Centre No": ')
    Data = Data.replace("Regist:", '\nRegist:')
    Data = Data.replace("Sat for 2 or more Subjects:", '\nSat for 2 or more Subjects: ')
    Data = Data.replace("Results of Successful Candidates In Order Of Merit", "")
    Data = Data.replace("% Passed : ", '\n%Passed: ')
    Data = Data.replace(" Passed : ", '\nPassed: ')
    print(Data)
    # Data = Data.replace("Sanctioned : ", '\nSanctioned: \n')

    # Replacing the Passed in x subjects section
    # Data = Data.replace("Passed In 11 Subjects: ", '\nPassed In 11 Subjects:')
    # Data = Data.replace("Passed In 10 Subjects: ", ' \n\nPassed In 10 Subjects: ')
    # Data = Data.replace("Passed In 9 Subjects: ", '\nPassed In 9 Subjects:')
    # Data = Data.replace("Passed In 8 Subjects: ", ' \n\nPassed In 8 Subjects: ')
    # Data = Data.replace("Passed In 7 Subjects: ", '\nPassed In 7 Subjects:')
    # Data = Data.replace("Passed In 6 Subjects: ", ' \n\nPassed In 6 Subjects: ')
    # Data = Data.replace("Passed In 5 Subjects: ", '\nPassed In 5 Subjects:')
    # Data = Data.replace("Passed In 4 Subjects: ", ' \n\nPassed In 4 Subjects: ')
    
    # Data = Data.replace("( In 9 Subjects: 16", "")

    # Data = Data.replace("(", " (")
    
  


    # print(Data)
    # f.write(Data)

     
# =========================================================
                    #APPROACH 1: USE NAME, APPEND REGEX AND EXTRACT DATA

    # Prompting name
    while True:
        NameResult = input("What is the name: ")
        StudentName = NameResult

        #Concatenating name to regex for results
        NameResult = r"("+NameResult+").*?\("                              
        # NameResult = NameResult + " +\s?([A-Z]+-([A-E],?))+"

        # Printing out the combined regex before searching
        print('Sneak Preview of the RegExp')
        # print((NameResult))

        #Searching the combined regex in the extracted data
        # print('Processing')
        NameResult = re.search(r""+NameResult, Data)

        # print('**************************************************')
        Finale_NameResult = NameResult.group(0)[:-1]
        NameResult = NameResult.group(0)[:-1]
        print(Finale_NameResult)
        # print(NameResult)

        # print(type(NameResult.group(0)[:-1]))
        # print('**************************************************')

        #Initialising dictionary to push data to
        Finale_content = {}

        #Extract results from Finale_NameResult
        FinaleResult = re.search(r"([A-Z]+-[A-E] ,?)+", Finale_NameResult)
        FinaleResult = FinaleResult.group(0)
        # print(FinaleResult)

        #pushing name and result to the dictionary
        Finale_content[StudentName] = FinaleResult

        subjects = FinaleResult.split(",")



        
        displaypassed = "Congratulations {name}. You Passed in {num} subjects which are {Resulthere}".format(name = StudentName, num = len(subjects), Resulthere = FinaleResult)
        # len(subjects)


        print('\n\n\n**************************Processing*********************\n')
        print(Finale_content)
        print(displaypassed)
        print('\n*********************************************************')
        print("\n\n\n")

    # ==================================================
                        #APPROACH #2
                # FIND ANY NAME AND RESULTS LINKED TOGETHER 

        result_and_name = re.findall(r"(([A-Z]-?'?)+ .*?\()", Data)
        # print(len(result_and_name))
        # print((result_and_name))
        # print(type(result_and_name))
        subresults = []
        for i in result_and_name:
            # i[2:-9]
            i = str(i)
            i = i[2:-9]
            # print(type(i))
            subresults.append(i)
            # print(i)
        import json
        subresults = json.dumps(subresults)
        # print(subresults)

        # f.write(subresults)
        # f.close()

    # =======================================================================================================
                            #EXTRACTING RESULTS AND NAME FROM EXTRACTED LINKED DATA

    for i in subresults:
    #    Name =  re.search("[A-Z]{3}-[A-E],?", i)
       Name =  re.match("[A-Z]+-[A-E]", i)
    #    print(Name)
    #print(Name.group(0))






    # done = list(filter(lambda x:len(x) > 3, result_and_name))
    # print(done)

    # finale2  = " ".join(result_and_name)
    # result_and_name = re.findall("(([A-Z]+ )+.*?\()", result_and_name)

    # print((result_and_name))
    # fin = re.findall("(([A-Z]+ )+.*?\()", strin)
    # print(result_and_name)
# Get_Oldata("Olgen.txt")
Get_Oldata("./pdfs/2019-olgen.pdf")







#======================================================================================================================
                                            # PDF MERGER
#======================================================================================================================

# import PyPDF4 
# from PyPDF4 import PdfFileMerger
# pdfs = ["all_tech.pdf", "2019-olgen.pdf"]
# merger = PdfFileMerger()
# for pdf in pdfs:
#     merger.append(pdf)
# merger.write("alltech+algen.pdf")
# merger.close()

#
#RecursionError: maximum recursion depth exceeded while calling a Python object

















#======================================================================================================================
                                        # TEST FILE
#======================================================================================================================
# import re

# txt = "The rain in Spain and after the following, there is (7) another The Spain What wrong (8) what abou the rest (9)"
# x = re.search(r"(Spain and).*?\(", txt)

# print(x)
# # if type(x) == 'None':
# print(x.group(0))
#==============================================
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

# ==========================================================
# list = ["NSOH AKAME SHARON LIT-E,HIS-D,PHI-E", "NJINUWOH ANTHIONE TASSAH LIT-E,HIS-C", "NFORMI SHEKINAH-GLORY YULA ENG-C,LIT-E", "AKWO NGWA BEATRICE ECO-E,GEO-E", "MBUI ZEPHANIAH ASELIKWE ECO-E,GEO-E", "EKUKA CYNTHIA KIRA ECO-D,GEO-D,HIS-E", "CHIANKEM LAURENTINE CHIAFIE TENGIM BIO-B,CHE-D,PMM-E,PHY-D,ICT-C", "MUATEH YEYE GLORY ENG-D,LIT-E,HIS-B,PHI-A", "MISSI CYNTHIA PENGHA ECO-C,LIT-E,HIS-B,PHI-D", "GLORY MBUDZI ECO-A,ENG-E,GEO-E,HIS-C", "WIRBA RASMIRATU DZELAMONYUY ECO-B,ENG-D,GEO-E,HIS-C","NDUMBI SHALOM MANKA'A BIO-D,PMS-C"]
# =============================================================

string = "ZACHUO REBONA COM-C ,ECO-C ,FRE-C ,GEO-C ,HIS-C ,CZE-B ,LOG-C  (32)NGORAN FALIATU WIYKIYNYUY BIO-C ,CHE-C ,ECO-C ,ENG-C ,FRE-C ,GEO-B ,MAT-C  (33)MUNGE NGOME SHULETTE COM-C ,ECO-C ,ENG-B ,LIT-C ,FRE-C ,GEO-C ,CZE-C  (34)NGWENUI YVETTE BETSUEDE COM-C ,ECO-C ,ENG-C ,LIT-C ,GEO-B ,HIS-C ,REL-C  (35)NJUA ALEXANDER BIO-C ,CHE-C ,ECO-B ,ENG-C ,GEO-C ,HBI-C ,PHY-C  (36)NGI DELEGENT BIO-C ,CHE-C ,ECO-B ,FRE-C ,GEO-C ,MAT-C ,PHY-C  (37)SHADIA SHEMENI HUOMBGE COM-C ,ECO-C ,ENG-C ,FRE-C ,GEO-C ,HIS-C ,CZE-C  (38)LUKONG NYUYYENI CLOVIS COM-C ,ECO-C ,ENG-C ,FRE-C ,GEO-C ,CZE-C ,MAT-C  (39)ACHA YANICK FOMBENG BIO-C ,CHE-C ,ECO-C ,ENG-C ,FRE-C ,GEO-C ,PHY-C NCHANG GLORY NGWA BIO-C ,CHE-C ,ECO-C ,ENG-C ,GEO-C ,HBI-C ,PHY-C  (41) "

# [A-Z]{3}-[A-E],?
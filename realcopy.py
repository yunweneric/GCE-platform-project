# 1: Importing dependecies
import PyPDF4


def Get_data(gce):
    # 2: Reading pdf
    Files = open(gce, 'rb')

    # 3: Loading files
    Loaded_pdf = PyPDF4.PdfFileReader(Files)

    # 4: saving content to a string called content
    content = Loaded_pdf.numPages
    # f = open("Algen.txt", "w")
    # 4.1: looping through all pages to access modify content
    for i in range(content):
        # 4.2: Reading(looping through all pages)
        page = Loaded_pdf.getPage(i)

        # 4.3: Extracting raw data
        Raw_data = page.extractText()

        # 4.4: Replacing bannar
        Data = Raw_data.replace("2019 RESULTS: GCE ADVANCED LEVEL GENERAL", "")

        # 4.5: Editing the name section
        # Data = Data.replace("(", "")
        # Data = Data.replace(")", ".")

        # Using regex
        import re
        Data = Data.replace("\n", "")
        Data = re.sub(r"\d+.\d+of\d+\w+", "", Data)
        # Data = re.sub(r"[A-Z]\d+", "", Data)
        # Data = re.sub(r"\d+[a-z]", "", Data)
        Data = Data.replace("Centre No:  ", '\n\n\n\n"Centre No": ')
        Data = Data.replace("Regist:", '\nRegist:')
        Data = Data.replace("Sat for 2 or more Subjects:", '\nSat for 2 or more Subjects: ')
        Data = Data.replace("Results of Successful Candidates In Order Of Merit", "")
        Data = Data.replace("% Passed : ", '\n%Passed: ')
        Data = Data.replace(" Passed : ", '\nPassed: ')
        Data = Data.replace("Sanctioned : ", '\nSanction: ')

        # Replacing the Passed in x subjects section
        Data = Data.replace("Passed In 5 Subjects: ", '\nPassed In 5 Subjects:')
        Data = Data.replace("Passed In 4 Subjects: ", ' \n\nPassed In 4 Subjects: ')
        Data = Data.replace("Passed In 3 Subjects: ", ' \n\nPassed In 3 Subjects: ')
        Data = Data.replace("Passed In 2 Subjects: ", ' \n\nPassed In 2 Subjects: ')
        Data = re.sub(r"Passed In \d Subjects: \d+", "", Data)
        Data = re.sub(r"Passed In \d Subjects:\d+", "", Data)
        Data = Data.replace("(", " (")



        # Data = Data.split(".")
        # Data = Data.join("")

        print(Data)


        # print("NDUMBI SHALOM MANKA'A" in Data)
        # print(Data[1])
        # f.write(Data+"\n")
    # f.close()


# FONKENG ESENDENGE GLEN-RODNEY (BIO-\W,?)? CHE-\W,?|PMS-\W,?|PHY-\W,?|ICT-\W,?|ECO-\W,?|FRE-\W,?|GEO-\W,?|HIS-\W,?|PHI-\W,?|LIT-\W,?|REL-\W,?|PMM-\W,?|FSN-\W,?|ENG-E\W,?"


    #Prompting name
    NameResult = input("What is the name: ")
    NameResult = NameResult + " ([A-Z]+-[A-E],?)+"
    print((NameResult))

    NameResult = re.search(NameResult, Data)
    # print(type(NameResult))   


    print(NameResult);



















        # approach2 

        #demand the name, or use common names
        #1.1. Consider all the possible names, comma seperated names, names with hyphens
        #Or
        #Automatically/ Dynamically find any pattern
        #append the possible results seperated by or (|) example BIO-\W|,CHE-\W|,PMS-\W|,PHY-\W|,ICT-\W|ECO-\W|,FRE-\W|,GEO-\W|,HIS-\W|,PHI-\W|LIT-\W|,REL-\W|PMM-\W|,FSN-\W|,ENG-E\W
        #pass this to a regex

        #splice out name and store in a variable
        #splice out results and store in a variable
        #Initialise an empty dictionary
        #Push name and results to a dictionary in the form("NAME":"RESULTS")
        #Cut out results from main database so that we know there is completion








 
# FONKENG ESENDENGE GLEN-RODNEY BIO-B,CHE-C,PMS-C,PHY-E,ICT-C (1)TALONFO ZUEKO CURIE L ECO-E,FRE-E,GEO-E,HIS-C,PHI-D (2) 

# TACHE JENIFER ANDUH BIO-C,CHE-B,PMS-A,PHY-C(1)MBONDE PAUL NKEZE ENG-D,LIT-D,HIS-B,PHI-B(
 

# NDI HARIETTE BONSAW BIO-B,CHE-E,FSN-B,PMS-D(3)MBI CHRISTABEL AKUM LIT-D,HIS-B,REL-C,PHI-D(4)NKENG NALDINE MANYI BIO-C,CHE-C,PMS-C,ICT-E(5)EYOME MAIRA BIO-B,CHE-E,FSN-B,PHY-E(6)FORZI DEFANG JOSHUA BIO-C,CHE-E,PMS-C,PHY-D(7)ATABONGAFAC DAVID AWUNG LIT-E,HIS-B,REL-E,PHI-D(8) 

# NEDAN NDOME CORINE DANIELLE ECO-D,GEO-E,PMS-C(1)NGOE ELIZABETH ELOLE LIT-E,HIS-B,REL-E(2) 

# NDUMBI SHALOM MANKA'A BIO-D,PMS-C(





























Get_data("2019-algen.pdf")



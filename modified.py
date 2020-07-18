#=======================================================================================================================                  
# 1: Importing dependecies
import PyPDF4

def Get_data(gce):
    # 2: Reading pdf #1.3. splice out name and store in a variable
    Files = open(gce, 'rb')

    # Initialize the Raw data container
    Raw_data = ""

    # 3: Loading files
    Loaded_pdf = PyPDF4.PdfFileReader(Files)

    # 4: saving content to a string called content
    content = Loaded_pdf.numPages

    # 4.1: looping through all pages to access modify content
    for i in range(content):
        # 4.2: Reading(looping through all pages)
        page = Loaded_pdf.getPage(i)

        #1.3. splice out name and store in a variable
        # 4.3: Extracting raw data
        Raw_data = Raw_data + "" + page.extractText()
        # 4.4: Replacing bannar

    Data = Raw_data.replace(" ","")
    Data = Data.replace("2019 RESULTS: GCE ADVANCED LEVEL GENERAL", "")
    Data = Data.replace("2019RESULTS:GCEORDINARYLEVELGENERAL", "")
    Data = Data.replace("2019 RESULTS: GCE ORDINARY LEVEL TECHNICAL", "")
    Data = Data.replace("2019 RESULTS: GCE ADVANCED LEVEL TECHNICAL", "")

    

    # 2019 RESULTS: GCE ORDINARY LEVEL GENERAL
    # Reorganising work using Using regex and string methods
    import re
    Data = Data.replace("\n", "")
    # Data = re.sub(r"\d+.\d+of\d+\w+", "", Data)
    # Data = Data.replace("CentreNo:  ", '\n\n\n\n"Centre No": ')
    # Data = Data.replace("Regist:", '\nRegist:')
    # Data = Data.replace("Sat for 2 or more Subjects:", '\nSat for 2 or more Subjects: ')
    # Data = Data.replace("Results of Successful Candidates In Order Of Merit", "")
    # Data = Data.replace("% Passed : ", '\n%Passed: ')
    # Data = Data.replace(" Passed : ", '\nPassed: ')
    # Data = Data.replace("Sanctioned : ", '\nSanctioned: ')

    Data = re.sub(r"\d+.\d+of\d+\w+", "", Data)
    Data = re.sub(r"Regist:", "\nRegisted:", Data)
    Data = re.sub(r"CentreNo:", "\nCentre No: ", Data)
    Data = re.sub(r"Sanctioned:\d+", "", Data)
    Data = re.sub(r"%Passed:", "\n%Passed", Data)
    Data = re.sub(r"Satfor2ormoreSubjects:", "\nSat for 2 or more Subjects:", Data)
    Data = re.sub(r"Passed:", "\nPassed", Data)
    Data = Data.replace("CentreNo:  ", '\n\n\n\n"Centre No": ')
    Data = Data.replace("Regist:", '\nRegist:')
    Data = Data.replace("Satfor2ormoreSubjects:", '\nSat for 2 or more Subjects: ')
    Data = Data.replace("ResultsofSuccessfulCandidatesInOrderOfMerit", "")
    Data = Data.replace("%Passed : ", '\n%Passed: ')
    Data = Data.replace(" Passed : ", '\nPassed: ')
    Data = Data.replace("Sanctioned : ", '\nSanctioned: ')



    # Replacing the Passed in x subjects section
    Data = Data.replace("Passed In 5 Subjects: ", '\nPassed In 5 Subjects:')
    Data = Data.replace("Passed In 4 Subjects: ", ' \n\nPassed In 4 Subjects: ')
    Data = Data.replace("Passed In 3 Subjects: ", ' \n\nPassed In 3 Subjects: ')
    Data = Data.replace("Passed In 2 Subjects: ", ' \n\nPassed In 2 Subjects: ')
    Data = re.sub(r"PassedIn\d+Subjects: \d+", "", Data)
    Data = re.sub(r"PassedIn\d+Subjects:\d+", "", Data)
    Data = Data.replace("(", " (")
    # print(Data)
        # return Data;


        # f.write(Data+"\n")
    # f.close()

    # Prompting name

    # NameResult = input("What is the name: ")
    # StudentName = NameResult

    # #Concatenating name to regex for results
    # NameResult = "("+NameResult+").*?\("                              

    # # NameResult = NameResult + " +\s?([A-Z]+-([A-E],?))+"

    # # Printing out the combined regex before searching
    # # print('Sneak Preview of the RegExp')
    # # print((NameResult))

    # #Searching the combined regex in the extracted data
    # # print('Processing')
    # NameResult = re.search(r""+NameResult, Data)

    # # print('**************************************************')
    # Finale_NameResult = NameResult.group(0)[:-1]
    # print(Finale_NameResult)

    # # print(type(NameResult.group(0)[:-1]))

    # # print('**************************************************')

    # #Initialising dictionary to push data to
    # Finale_content = {}

    # #Extract results from Finale_NameResult
    # FinaleResult = re.search(r"([A-Z]+-[A-E],?)+", Finale_NameResult)
    # FinaleResult = FinaleResult.group(0)
    # # print(FinaleResult)

    # #pushing name and result to the dictionary
    # Finale_content[StudentName] = FinaleResult

    # subjects = FinaleResult.split(",")



    
    # displaypassed = "Congratulations {name}. You Passed in {num} subjects which are {Resulthere}".format(name = StudentName, num = len(subjects), Resulthere = FinaleResult)
    # # len(subjects)


    # print('\n\n\n**************************Processing*********************\n')
    # print(Finale_content)
    # print(displaypassed)
    # print('\n*********************************************************')
    # print("\n\n\n")


    result_and_name = re.findall(r"(([A-Z]-?'?)+.*?\()", Data)
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
        print(i)
    import json
    subresults = json.dumps(subresults)
    # print(subresults)

    
    # for i in subresults:
    #    Name =  re.search(r"([A-Z]{3}-[A-Z]{1},?)+", i)
    #    print(Name)
    #    print(Name.group(0))







    # done = list(filter(lambda x:len(x) > 3, result_and_name))
    # print(done)

    # finale2  = " ".join(result_and_name)
    # result_and_name = re.findall("(([A-Z]+ )+.*?\()", result_and_name)

    # print((result_and_name))
    # fin = re.findall("(([A-Z]+ )+.*?\()", strin)
    # print(result_and_name)
Get_data("./pdfs/2019-olgen.pdf")
#=======================================================================================================================
# /home/yunwen/Documents/Seven Advanced/Projects/GCE-platform-project/pdfs/2019-algen.pdf
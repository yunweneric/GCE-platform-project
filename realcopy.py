#=======================================================================================================================                    
                    # APPROACH 

        #1.0 Request the name with a prompt, or use common names
        #1.1. Consider all the possible names, comma seperated names, names with hyphens
        #1.2. concatenate name with regex for results to get a combined regex having name and results
        #1.3. using the combined regex, seach for it and return the match which will contain both name and result
        #1.4. splice out results and store in a variable
        #1.5. Initialise an empty dictionary
        #1.6. Push name and results to the dictionary in the form("NAME":"RESULTS")
        #1.7. splice out results from main raw content so that we know there is completion
#=======================================================================================================================




# 1: Importing dependecies
import PyPDF4

def Get_data(gce):
    # 2: Reading pdf #1.3. splice out name and store in a variable
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
    #1.3. splice out name and store in a variable
        # 4.3: Extracting raw data
        Raw_data = page.extractText()

        # 4.4: Replacing bannar
        Data = Raw_data.replace("2019 RESULTS: GCE ADVANCED LEVEL GENERAL", "")

        # Reorganising work using Using regex and string methods
        import re
        Data = Data.replace("\n", "")
        Data = re.sub(r"\d+.\d+of\d+\w+", "", Data)
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

        #Printing extracted data,
        print(Data)
        # f.write(Data+"\n")
    # f.close()

    #Prompting name
    NameResult = input("What is the name: ")

    #Concatenating name to regex for results
    NameResult = NameResult + " ([A-Z]+-[A-E],?)+"

    # NameResult = NameResult + " +\s?([A-Z]+-([A-E],?))+"

    #Printing out the combined regex before searching
    print((NameResult))

    #Searching the combined regex in the extracted data
    NameResult = re.search(NameResult, Data)

    # print(type(NameResult))   
    print(NameResult);
Get_data("2019-algen.pdf")
#=======================================================================================================================

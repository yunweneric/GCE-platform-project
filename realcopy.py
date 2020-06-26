#=======================================================================================================================                    
                    # Corrected Errors

        #1.0  Your indenting with the for loop in Get_Data function was a reason your data contained only the last page
        #1.1. You also did not concatenate the Raw_data of the first page to that of the other page too, soo you just overwrite them
        #1.2. I Didnt understant your regular expression,so i wrote mine to match from the name, down until the the first (
        #1.3. I used group(0) to extract the matching text and i spliced the ( with a [:-1] 

#=======================================================================================================================




# 1: Importing dependecies
import PyPDF4

def Get_data(gce):
    # 2: Reading pdf #1.3. splice out name and store in a variable
    Files = open(gce, 'rb')

    # Initialize the Raw data container
    Raw_data = " "

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
        Raw_data = Raw_data + " " + page.extractText()

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
        # return Data;


        # f.write(Data+"\n")
    # f.close()

    #Prompting name
    NameResult = input("What is the name: ")

    #Concatenating name to regex for results
    NameResult = "("+NameResult+").*?\(";

    # NameResult = NameResult + " +\s?([A-Z]+-([A-E],?))+"

    # Printing out the combined regex before searching
    print('Sneak Preview of the RegExp')
    print((NameResult))

    #Searching the combined regex in the extracted data
    print('Processing')
    NameResult = re.search(r""+NameResult, Data)

    print('**************************************************')
    print(NameResult.group(0)[:-1]) 
    print('**************************************************')
Get_data("2019-algen.pdf")
#=======================================================================================================================

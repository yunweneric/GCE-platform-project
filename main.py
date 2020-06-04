# #1: Importing dependecies
import PyPDF4
#2: Reading pdf
File = open('2019-algen.pdf', 'rb')

#3: Loading files
Loaded_pdf = PyPDF4.PdfFileReader(File)

#4: saving content to a string called content
content = Loaded_pdf.numPages
#5: looping through all pages to access modify content
def Get_data():
    for i in range(content):
        #5.1: Reading(looping through all pages)
        page = Loaded_pdf.getPage(i)
        print(str(1 + Loaded_pdf.getPageNumber(page)))
        pagecontent = page.extractText()
        print(pagecontent)
        #5.2: Saving raw data
        Raw_data = page.extractText()


        # Raw_data = str(Raw_data)
        #5.3: Replacing bannars
        #Data = Raw_data.replace("2019 RESULTS: GCE ADVANCED LEVEL GENERAL", "2019 RESULTS GCE ADVANCED LEVEL GENERAL = {")
        # Data = Raw_data.replace("2019 RESULTS: GCE ADVANCED LEVEL GENERAL","")

        #5.4: Editing the info section
        # Data = Data.replace("Centre No:  ", '\n"info": {\n\t"Centre No": ')
        # Data = Data.replace("Regist:", '\n\t"Regist":')
        # Data = Data.replace("Sat for 2 or more Subjects:", '\n\t"Sat for 2 or more Subjects": ')
        # Data = Data.replace("Results of Successful Candidates In Order Of Merit", "")
        # Data = Data.replace("% Passed : ", '\n\t"%Passed": ') 
        # Data = Data.replace(" Passed : ", '\n\t"Passed": ')
        # Data = Data.replace("Sanctioned : ", '\n\t"Sanction": ')
        # Data = Data.replace("(", "\n")
        # Data = Data.replace(")", ".")

        #Replacing the Passed in x subjects section
        # Data = Data.replace("Passed In 5 Subjects: ", '\n\t} \n\n"Passed In 5 Subjects":')
        # Data = Data.replace("Passed In 4 Subjects: ", ' \n\n"Passed In 4 Subjects": ')
        # Data = Data.replace("Passed In 3 Subjects: ", ' \n\n"Passed In 3 Subjects": ')
        # Data = Data.replace("Passed In 2 Subjects: ", ' \n\n"Passed In 2 Subjects": ')

        #Using Regular  Expressions
        # import re
        # Data = re.sub("\d+\.\d+[a-z]+\d+[A-Z]+[a-z]+", " ", Data)
        print (Raw_data)
        # print(type(Raw_data))
Get_data()
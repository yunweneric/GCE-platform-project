# #1: Importing dependecies
import PyPDF4


#2: Merging all available pdfs (Cannot merge all files for now!)
# from PyPDF4 import PdfFileMerger
# pdfs = ["2019-algen.pdf", "2019-altech.pdf", "2019-olgen.pdf", "2019-oltech.pdf"]
# merger = PdfFileMerger()
# for pdf in pdfs:
#     merger.append(pdf)
# merger.write("all.pdf")
# merger.close()



#2: Reading pdf
Files = open('2019-algen.pdf', 'rb')

#3: Loading files
Loaded_pdf = PyPDF4.PdfFileReader(Files)

#4: saving content to a string called content
content = Loaded_pdf.numPages


# #6: looping through all pages to access modify content
for i in range(content):
    #6.1: Reading(looping through all pages)
    page = Loaded_pdf.getPage(i)
    
    #6.2: Saving raw data
    Raw_data = page.extractText()

    #6.3: Replcaing bannars
    Data = Raw_data.replace("2019 RESULTS: GCE ADVANCED LEVEL GENERAL", "2019 RESULTS GCE ADVANCED LEVEL GENERAL = {")

    
    #6.Modifying center number
    Data = Data.replace("Centre No:  ", "info = {\n             Centre No: ")

    #Modifying Register
    Data = Data.replace("Regist", ", Regist")

    Data = Data.replace("Passed in : ", "} Passed : ")


    # Data = Raw_data.replace("Results", "\nResults")
    # Data = Data.replace("Results", "\nResults")
    Data = Data.replace("Results of Successful Candidates In Order Of Merit", "")    
    # Data = Data.replace("% Passed : ", "Passed : ")
    
    # Data = Data.replace("Sanctioned : ", "\nSanction : ")
    # Data = Data.replace("Results of Successful Candidates In Order Of Merit : ", "\nResults of Successful Candidates In Order Of Merit")
    # Data = Data.replace("Sat for 2 or more Subjects:", "\nSat for 2 or more Subjects:")
    # Data = Data.replace("Passed In 5 Subjects: ", " \n\nPassed In 5 Subjects: ")
    # Data = Data.replace("Passed In 4 Subjects: ", " \n\nPassed In 4 Subjects: ")
    # Data = Data.replace("Passed In 3 Subjects: ", " \n\nPassed In 3 Subjects: ")
    # Data = Data.replace("Passed In 2 Subjects: ", " \n\nPassed In 2 Subjects: ")
    Data = Data.replace("(", "")
    Data = Data.replace(")", ". ")
    print((Raw_data))


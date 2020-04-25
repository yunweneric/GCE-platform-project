# import PyPDF2
# My_file = PyPDF2.PdfFileReader("2019-algen.pdf")
# Pagenumber = My_file.getNumPages()
# page_ze = My_file.getPage(0)
# count = pdfReader.numPages
import PyPDF2
A_file = open('2019-algen.pdf', 'rb')
Load_file = PyPDF2.PdfFileReader(A_file)
count = Load_file.numPages
for i in range(count):
    page = Load_file.getPage(i)
    Raw_data = page.extractText()
    Data = Raw_data.replace("Results", "\nResults")
    Data = Data.replace("Centre No:  ", " \nCentre No: ")
    Data = Data.replace("Regist", "\nRegist")
    Data = Data.replace("% Passed : ", "\n%Passed : ")
    Data = Data.replace(", Passed : ", "\nPassed : ")
    Data = Data.replace("Sanctioned : ", "\nSanction : ")
    Data = Data.replace("Results of Successful Candidates In Order Of Merit : ", "\nResults of Successful Candidates In Order Of Merit")

    Data = Data.replace("Sat for 2 or more Subjects:", "\nSat for 2 or more Subjects:")
    Data = Data.replace("Passed In 5 Subjects: ", " \n\nPassed In 5 Subjects: ")
    Data = Data.replace("Passed In 4 Subjects: ", " \n\nPassed In 4 Subjects: ")
    Data = Data.replace("Passed In 3 Subjects: ", " \n\nPassed In 3 Subjects: ")
    Data = Data.replace("Passed In 2 Subjects: ", " \n\nPassed In 2 Subjects: ")
    Data = Data.replace("(", "\n")
    Data = Data.replace(")", ". ")
    print(Data)


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
        # Data = Data.split(".")
        # Data = Data.join("")

        print(Data)


        # print("YOH RODRICK YUH" in Data)
        # print(Data[1])
        # f.write(Data+"\n")
    # f.close()
Get_data("2019-algen.pdf")

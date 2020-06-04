#1: Importing dependecies
import PyPDF4

def Get_data(gce):
    #2: Reading pdf
    Files = open(gce, 'rb')

    #3: Loading files
    Loaded_pdf = PyPDF4.PdfFileReader(Files)

    #4: saving content to a string called content
    content = Loaded_pdf.numPages
    f = open("Algen.txt", "w")
    #4.1: looping through all pages to access modify content
    for i in range(content):
        #4.2: Reading(looping through all pages)
        page = Loaded_pdf.getPage(i)
        
        #4.3: Extracting raw data
        Raw_data = page.extractText()

        #4.4: Replacing bannar
        Data = Raw_data.replace("2019 RESULTS: GCE ADVANCED LEVEL GENERAL", "")

        #4.5: Editing the name section
        Data = Data.replace("(", "")
        Data = Data.replace(")", ".")

        #Using regex
        import re
        Data = re.sub("\d+\.\d+[a-z]+\d+[A-Z]+[a-z]+", " ", Data)
        
        print(type(Data)) 
        # f.write(Data+"\n")
    f.close()
Get_data("2019-algen.pdf")

#================================================================================================================

                                    #Working with text file

#================================================================================================================
# text = open("Algen.txt", "rb")
# text_content = text.read()
# for i in text_content: 
#     text_content = text_content.decode(encoding = "utf-8")
#     print(text_content)

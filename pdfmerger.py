import PyPDF4 
from PyPDF4 import PdfFileMerger
# pdfs = ["2019-altech.pdf", "2019-oltech.pdf"]
# merger = PdfFileMerger()
# for pdf in pdfs:
#     merger.append(pdf)
# merger.write("all_tech.pdf")

pdfs = ["all_tech.pdf", "2019-olgen.pdf"]
merger = PdfFileMerger()
for pdf in pdfs:
    merger.append(pdf)
merger.write("alltech+algen.pdf")
merger.close()

#
#RecursionError: maximum recursion depth exceeded while calling a Python object
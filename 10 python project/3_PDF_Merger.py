from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []

n = int(input("No. of pdf u want to merge: "))

for i in range(0, n):
    name = input(f"Enter the name if pdf {i + 1}: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.closed()
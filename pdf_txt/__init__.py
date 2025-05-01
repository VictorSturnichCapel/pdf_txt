from PyPDF2 import PdfReader

reader = PdfReader("file.pdf")
page = reader.pages[3]

with open("output.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write(page.extract_text())
from PyPDF2 import PdfReader

with open("sample.pdf", "rb") as file:  # file gets opened
    reader = PdfReader(file)  # this helps in reading the file
    page = reader.pages[1]  # first page of the pdf is pulled
    text = page.extract_text()  # extracts the content from the file
    print(text)

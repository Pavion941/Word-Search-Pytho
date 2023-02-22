from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

#method that deals with pdf's
def pdf_handler():
    file_Path = input("Enter the PDF file path: ")
    output_string = StringIO()
    
    with open(file_Path, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    #saved the contents of the selected PDF into a stringIO type variable

    #TEST print(output_string.getvalue())
    
    reg_string = output_string.getvalue() #saving contents of the StringIO variable into a regular string for searching
    lower_case_string = reg_string.lower() #creating a lower case version of the string so we can search without worrying about upper case
    
    #TEST print(lower_case_string)
    #TEST print(lower_case_string.count('cardiac resynchronization therapy'))
    
    count = lower_case_string.count('cardiac resynchronization therapy') #variable to save the number of times thing appears
    
    #print(count)
    #super stupid way of figuring out if related or not. Should work.
    if count > 0:
        print("This pdf is related to Cardiac Resynchronization Therapy")
    if count == 0:
        print("This pdf is not related to Cardiac Resynchronization Therapy")
 

#method for handling txt files 
def txt_handler():
    txt_file_Path = input("Enter the txt file path: ")

    with open(txt_file_Path, 'r') as file:
        text = file.readlines()

    #TEST type(text) this is a list
    str = ""  #empty string to hold the contents of the txt file

    for ele in text:  # loop through list and add each element to the empty string
        str += ele

    #print(str)
    lower_case_str = str.lower() #make sure its all lower case because python is case sensitive
    count = lower_case_str.count('cardiac resynchronization therapy') #variable to count thing
    #print(count)
    #type(str)
    #print(lower_case_txt_string)
    if count > 0:
        print("This pdf is related to Cardiac Resynchronization Therapy")
    if count == 0:
        print("This pdf is not related to Cardiac Resynchronization Therapy")

loop = True

while loop:
    choice = input ("Enter 1 if the file is a PDF and 2 if the file is txt: ")
    if choice == '1':
        pdf_handler()
        loop = False
    elif choice == '2':
        txt_handler()
        loop = False
    else:
        print("Invalid option entered.")
        
# installing libraries
import pyttsx3
import PyPDF2


book = open('mycv.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
for i in range(0, pdfReader.numPages):
    page = pdfReader.getPage(i)
    text = page.extractText()
    alexa = pyttsx3.init()
    alexa.say(text)
    alexa.runAndWait()


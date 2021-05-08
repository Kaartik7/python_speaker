import pyttsx3
import PyPDF2


def read_my_cv():
    """
    Program that reads my cv.
    """
    book = open('mycv.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    for i in range(0, pdfReader.numPages):
        page = pdfReader.getPage(i)
        text = page.extractText()
        alexa = pyttsx3.init()
        alexa.say(text)
        alexa.runAndWait()

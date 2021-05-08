# installing libraries
from weather_api import get_weather
import pyttsx3
import PyPDF2
from datetime import date



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

def day_date_time():
    """
    Reads out today's date.
    """
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    alexa = pyttsx3.init()
    alexa.say(d2)
    alexa.runAndWait()

def weather_report(city: str):
    """
    Program that uses OpenWeatherAPI to read out the weather report of a given city.
    """
    report = get_weather(city)
    alexa = pyttsx3.init()
    alexa.say(report)
    alexa.runAndWait()



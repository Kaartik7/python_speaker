
import pyttsx3
from datetime import date


def day_date_time():
    """
    Reads out today's date.
    """
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    alexa = pyttsx3.init()
    alexa.say(d2)
    alexa.runAndWait()





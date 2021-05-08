# installing libraries
from weather_api import get_weather
import pyttsx3



def weather_report(city: str):
    """
    Program that uses OpenWeatherAPI to read out the weather report of a given city.
    """
    report = get_weather(city)
    alexa = pyttsx3.init()
    alexa.say(report)
    alexa.runAndWait()


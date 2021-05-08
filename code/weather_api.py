
import requests
import json
def get_weather(cityname):

    api_key = "" #Enter your key here
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + cityname

    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    if x["cod"] != "404":

        y = x["main"]

        temperature_now = y["temp"]

        pressure_now = y["pressure"]

        humidiy_now = y["humidity"]

        z = x["weather"]

        description = z[0]["description"]

        # print following values
        weather_report = (" Temperature is " +
              str(temperature_now) +
              " atmospheric pressure is " +
              str(pressure_now) +
              " humidity is " +
              str(humidiy_now) +
              " description is " +
              str(description))

    else:
        weather_report = " City Not Found "
    return weather_report

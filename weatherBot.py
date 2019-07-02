#! /usr/bin/python3
#Program used to get weather and text myself

import requests
import webbrowser
import pyowm
import smtplib

owm = pyowm.OWM('***API KEY***') #valide api key w/ server

location = 'Fort Worth, USA' #Change to anything you want

observation = owm.weather_at_place(location)
w = observation.get_weather()
print(w.get_temperature('fahrenheit')["temp_max"])#Grabs only the temperature

x = w.get_temperature('fahrenheit')["temp_max"]

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
type(smtpObj)
smtpObj.starttls()
smtpObj.login('***EMAIL***', '***PASSWORD***')
smtpObj.sendmail('***FROM_EMAIL***', '***TO_EMAIL***', 'Subject: Weather Report.\nHello, the weather today is as follows.\n\nIt is currently ' + str(x) + ' in ' + location + '\n\nHave a wonderful day.')

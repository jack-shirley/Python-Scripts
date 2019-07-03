#! /usr/bin/python3
#Program used to get weather and text myself

import requests
import webbrowser
import pyowm
import smtplib

api_key = '***API_KEY***'
owm = pyowm.OWM(api_key) #valide api key w/ server

# Customize these variables
login_email = '***EMAIL***'
password = '***PASSWORD***'
from_email = '***FROM_EMAIL***'
to_email = '***TO_EMAIL***'
location = 'Fort Worth, USA' #Change to anything you want

# Retrieves the weather from the API
observation = owm.weather_at_place(location)
w = observation.get_weather()

# Gets the main temperatures for the day
temp = w.get_temperature('fahrenheit')["temp"]
temp_max = w.get_temperature('fahrenheit')["temp_max"]
temp_min = w.get_temperature('fahrenheit')["temp_min"]

print('Temperature in ' + location + ': ' + str(temp)) # Display the temperature

# Subject and message
subject = 'Subject: Weather Report.\n'
message = 'Hello, the weather is as follows.\n\n\
It is currently ' + str(temp) + ' in ' + location + '\n\n\
Have a wonderful day.'

# Start the SMTP server and send message
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login(login_email, password)
smtpObj.sendmail(from_email, to_email, subject + message)

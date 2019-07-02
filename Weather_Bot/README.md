# Weather Bot

Weather Bot is a simple Python script that makes use of the Open Weather API to fetch the temperature of your city,
and send you a text message telling you the temperature. For best results, store on a UNIX based operating system, and have
it run on crontab to inform you, and whoever you like of the weather daily.

## Prerequisites

- Python 2/3
- Raspberry Pi / UNIX Operating System (Not Required)

## Setup

Simply replace the following with their corresponding data:

- ***API_KEY*** : Go to https://openweathermap.org/api and obtain an API key
- ***EMAIL*** : Your email address (Preferably Gmail, or modification to script may be needed if not)
- ***PASSWORD***: Your email password
- ***FROM_EMAIL***: The email for the data to be sent to, most likely your email from earlier
- ***TO_EMAIL***: The recipient's email or SMS/MMS gateway

#### SMS/MMS Gateway Setup (Optional)

If you would rather the script send you an SMS message of the weather, this can simply be done depending on your carrier.
Change the FROM_EMAIL to one of these:

- AT&T : <Phone_Number>@txt.att.net
- Sprint: <Phone_Number>@messaging.sprintpcs.com
- T-Mobile: 001<Phone_Number>@tmomail.net
- Verizon: <Phone_Number>@vtext.com

#### Crontab Setup (Optional)

To have the script send an email/text daily (or however often you'd like), first move your script to

```
/etc/cron.daily/weatherBot.py
```

then open your crontab by using

```
crontab -e
```

and add the following line to the end of the file.

```
0 7 * * * /etc/cron.daily/weatherBot.py
```

This will run the script daily at 7am

### Authors

- Jack Shirley / www.github.com/jack-shirley

import os
import requests
from twilio.rest import Client


OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
weather_params = {
    "lat": 25.594095,
    "lon": 85.1375664,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
will_rain = False

for weather in weather_data['list']:
    if int(weather['weather'][0]['id']) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Don't forget to carry your umbrella. It might rain heavily.☔",
        from_='<twilio_number>',
        to='<your_number'
    )

    print(message.status)

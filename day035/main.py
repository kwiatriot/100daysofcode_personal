"""
Day 035 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 7/28/2022
Using environment veriables with API calls. Weather updates via SMS
"""

#Note! For the code to work you need to replace all the placeholders with
#Your own details. e.g. account_sid, lat/lon, from/to phone numbers.

import os
import requests
from twilio.http.http_client import TwilioHttpClient
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "ACb6027176f43ccaeab2683ff454e2ac1a"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": "39.98568173040156",
    "lon": "-104.7614145018273",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+18454470405",
        to=os.environ.get("VERIFIED_SMS")
    )
    print(message.status)

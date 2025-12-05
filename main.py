import requests
from twilio.rest import Client

# Data TWILIO
account_sid = "AC76409dca322f0fcb5a78dcd53495c914"
auth_token = "f950fa814171cc3d0cdf2b2dc0c73688"

# Data API
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "66f6cbad881273ef44939c4bca711829"
MY_LAT = -15.774898
MY_LONG = -47.880569

parameters = {
    'lat': -22.901449,
    'lon': -43.178921,
    'appid': api_key,
    'cnt': 4,
}

# Taking tha data of API
response = requests.get(OWN_ENDPOINT, params=parameters)
response.raise_for_status()

data = response.json()
list_of_data = data['list']
# [0]['weather'][0]['id']
list_of_id = [list_['weather'][0]['id'] for list_ in list_of_data]

will_rain = False
for id in list_of_id:
    if id < 700:
        will_rain = True


if will_rain:
    # Sending the message
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="+14245436338",
        to=my_number,
    )
    print(message.status)

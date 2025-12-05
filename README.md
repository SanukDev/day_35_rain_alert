Weather Alert via SMS


This project sends an SMS alert if rain is expected in the next few hours, using:
OpenWeatherMap API for weather forecasts
Twilio for sending SMS messages
Python (requests + twilio)


Overview


The script performs the following steps:
Requests weather forecast data from the OpenWeatherMap API.
Checks the next 4 forecast periods (about 12 hours).
Examines the weather condition codes returned by the API.
Codes below 700 indicate rain, drizzle, storms, snow, etc.
If any of these conditions are detected, the script sends an SMS alert using Twilio.

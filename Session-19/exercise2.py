import http.client
import json
import sys

# -- API information

city = input("Introduce a capital city: ")
HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/search/?query=" + city
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Read the response's body and close
# -- the connection
capital = r1.read().decode("utf-8")
conn.close()
info = json.loads(capital)

if len(info) == 0:
    print("The city does not exist or the web does not have the information")
    sys.exit()

woeid = info[0]['woeid']


ENDPOINT = "/api/location/"
conn.request(METHOD, ENDPOINT + str(woeid) + '/', None, headers)
r1 = conn.getresponse()

text_json = r1.read().decode("utf-8")
conn.close()

weather = json.loads(text_json)
time = weather['time']
temp0 = weather['consolidated_weather'][0]
description = temp0['weather_state_name']
temp = temp0['the_temp']
place = weather['title']
sun_set = weather['sun_set']

print()
print("Place: {}".format(place))
print("Time: {}".format(time))
print("Sunset time: {}".format(sun_set))
print("Weather description: {}".format(description))
print("Current temp: {} degrees".format(temp))
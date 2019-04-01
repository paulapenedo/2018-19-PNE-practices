import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT = "/jokes/random"
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}


conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Generate the object from the json file
jokes = json.loads(text_json)
print("The random joke about Chuck Norris is:", jokes['value']['joke'])

# Now i get the number of categories
ENDPOINT = "/categories"
conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

text_json = r1.read().decode("utf-8")
conn.close()

# -- Generate the object from the json file
total = json.loads(text_json)
categories = total ["value"]
print("The length of the categories is", len(categories))
for i in categories:
    print("One category is", i)

# Now I count the total number of jokes
ENDPOINT = "/jokes/count"
conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

text_json = r1.read().decode("utf-8")
conn.close()

# -- Generate the object from the json file
count_jokes = json.loads(text_json)
print("The total number of jockes about Chuck Norris are", count_jokes['value'])
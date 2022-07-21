import requests

# get the web page
response = requests.get("http://127.0.0.1:5000/crypto")
# convert the web page api to json
data = response.json()
# display data
print(data.get('bitcoin')['price'])
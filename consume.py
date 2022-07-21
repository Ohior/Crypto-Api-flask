import requests

response = requests.get("http://127.0.0.1:5000/crypto")
# response.raise_for_status
data = response.json()
print(data.get('bitcoin')['price'])
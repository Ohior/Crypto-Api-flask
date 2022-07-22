# Flask Api

Flask Api is an api built with Flask micro framework, that aims at provide to top 50 crypto traders.
It works by scrapping the a webpage, getting the clean data, storing the clean data in the database.
And it deletes the previous data and provides a new one every time the api is called.
Get the latest trading price, main price, volume price, fall change, rise change, all time high, liquidity

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies.

```bash or cmd
pip install requests
pip install bs4
pip install flask
pip install virtualenv
```

## Set Up

Create a project folder and change directory into it
Create a virtual environment ```python -m virtualenv venv```
Activate the virtual environment  

```bash
source venv\\scripts\\activate
```

```cmd
venv\\scripts\\activate 
```

## Using the Api

``` python
import requests

# get the web page
response = requests.get("http://127.0.0.1:5000/crypto")
# convert the web page api to json
data = response.json()
# display data
print(data.keys())
```

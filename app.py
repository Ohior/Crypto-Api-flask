from flask import Flask, jsonify
from cryptoDB.database_maker import CryptoDBHelper
from scrapper.crypto_scrapper import CryptoScrapper

# initialize
app = Flask(__name__)
cryptoScrapper = CryptoScrapper()
cryptHelper = CryptoDBHelper()

def convertContextToJson(context):
    # convert context that will be pass to the webpage to json
    data = dict()
    for c in context:
        name: list = c[0].split('\xa0')
        data[name[1].split(' ')[0].lower()] = {'name':name[1], 'price':c[1], 'main_price':c[2], 'volume_price':c[3], 'fall_change':c[4], 'rise_change':c[5], 'all_time_high':c[6], 'liquidity':c[7], }
    return data

# set the route to /crypto and the default request method is GET
# meaning you can only get from api but cannot post
@app.route('/crypto')
def index():
    # scrape the crypto website and get data and store in database
    cryptoScrapper.getTableRow()
    # get all the data from database in list format
    context = cryptHelper.selectFromDatabase()
    # convert it to json
    context: dict = convertContextToJson(context)
    # send it so that it can be use as an api
    return jsonify(context)
    
if __name__ == '__main__':
    app.run(debug=True)
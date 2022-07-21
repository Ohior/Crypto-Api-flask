from flask import Flask, jsonify
from cryptoDB.database_maker import CryptoDBHelper
from scrapper.crypto_scrapper import CryptoScrapper

app = Flask(__name__)
cryptoScrapper = CryptoScrapper()
cryptHelper = CryptoDBHelper()

def convertContextToJson(context):
    data = dict()
    for c in context:
        name: list = c[0].split('\xa0')
        data[name[1].split(' ')[0].lower()] = {'name':name[1], 'price':c[1], 'main_price':c[2], 'volume_price':c[3], 'fall_change':c[4], 'rise_change':c[5], 'all_time_high':c[6], 'liquidity':c[7], }
    return data

@app.route('/crypto')
def index():
    context = cryptHelper.selectFromDatabase()
    context: dict = convertContextToJson(context)
    return jsonify(context)
    
if __name__ == '__main__':
    cryptoScrapper.getTableRow()
    app.run(debug=True)
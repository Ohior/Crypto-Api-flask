from cryptoDB.cryptoDBhelper import CryptoDBHelper
from cryptoDB.dataclass import CryptoDataClass


class AddToDB(object):
    def addToDatabase(self, lines):
        table = []
        cryptoHelper  = CryptoDBHelper()
        cryptoHelper.createTable()
        for line in lines:
            l = line.split(';')
            l = l[0:len(l)-2]
            table.append(l)
            if(len(l) <= 1):continue
            cryptoHelper.insertIntoDatabase(
                CryptoDataClass(
                    name=l[1], price=l[2], main_price=l[3], volume_price=l[4],
                    liquidity=l[5], all_time_high=l[6], fall_change=l[7], rise_change=l[8]
                )
            )
        cryptoHelper.saveDatabase()
        return table
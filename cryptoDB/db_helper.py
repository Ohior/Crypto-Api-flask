from cryptoDB.database_maker import CryptoDBHelper
from cryptoDB.dataclass import CryptoDataClass


class DatabaseHelper(object):
    def addToDatabase(self, rows):
        table = []
        cryptoHelper  = CryptoDBHelper()
        cryptoHelper.createTable()
        for row in rows:
            # remove all the unnecessary characters in the row
            l = row[0].split(';')
            l = l[0:len(l)-2]
            table.append(l)
            # check if any of the row is empty
            if(len(l) <= 1):continue
            # add row to the database one at a time
            cryptoHelper.insertIntoDatabase(
                CryptoDataClass(
                    name=l[1], price=l[2], main_price=l[3], volume_price=l[4],
                    liquidity=l[5], all_time_high=l[6], fall_change=l[7], rise_change=l[8]
                )
            )
        # when finished adding to the database, save the database
        cryptoHelper.saveDatabase()
        return table
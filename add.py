
import io
from cryptoDB.cryptoDBhelper import CryptoDBHelper
from cryptoDB.dataclass import CryptoDataClass


cryptoHelper  = CryptoDBHelper()
cryptoHelper.createTable()
with io.open("fname.txt", "r") as f:
    for line in f.readlines():
        l = line.split(';')
        l = l[0:len(l)-2]
        if(len(l) <= 1):continue
        cryptoHelper.insertIntoDatabase(
            CryptoDataClass(
                name=l[1], price=l[2], main_price=l[3], volume_price=l[4],
                liquidity=l[5], all_time_high=l[6], fall_change=l[7], rise_change=l[8]
            )
        )



import sqlite3

from cryptoDB.dataclass import CryptoDataClass


coins_dc = CryptoDataClass()

TABLE_NAME = 'Coins'

class CryptoDBHelper(object):
    def __init__(self):
        self.con = sqlite3.connect('coins.db')
        self.cur = self.con.cursor()
        self.deleteAll
    
    def createTable(self):
        self.cur.execute(f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            name TEXT, price TEXT, volumePrice TEXT,
            riseChange TEXT, mainPrice TEXT, allTimeHigh TEXT,
            fallChange TEXT, liquidity TEXT
        )
        ''')
    
    def insertIntoDatabase(self, dataclass):
        insert  = self.cur.execute(f'''
        INSERT INTO {TABLE_NAME} VALUES (
            "{dataclass.name}","{dataclass.price}","{dataclass.volume_price}",
            "{dataclass.rise_change}","{dataclass.main_price}","{dataclass.all_time_high}",
            "{dataclass.fall_change}","{dataclass.liquidity}"
        )
        ''')
        return insert
    
    def selectFromDatabase(self):
        select = self.cur.execute(f'SELECT * FROM {TABLE_NAME}').fetchall()
        return select
    
    def deleteAll(self):
        self.cur.execute(f'DROP TABLE IF EXISTS {TABLE_NAME}')
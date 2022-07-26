import sqlite3

TABLE_NAME = 'Coins'

# class for creating database
class CryptoDBHelper(object):
    def __init__(self):
        self.con = sqlite3.connect('coins.db', check_same_thread=False)
        self.cur = self.con.cursor()
    
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
        # get all data from database and convert them to list
        select = self.cur.execute(f'SELECT * FROM {TABLE_NAME}').fetchall()
        return select
    
    def deleteAll(self):
        self.cur.execute(f'DROP TABLE IF EXISTS {TABLE_NAME}')
    
    def saveDatabase(self):
        self.con.commit()
    
    def closeConnection(self):
        self.con.close()
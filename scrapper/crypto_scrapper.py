import io
from bs4 import BeautifulSoup
import requests

COIN_URL = 'https://www.livecoinwatch.com'
# crypto_dict = {'name':'', 'price':0, 'main_price':0, 'volume_price':0, 'fall_change':0, 'rise_change':0, 'all_time_high':0}


class CryptoScrapper(object):
    def __init__(self) -> None:
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        self.url_page = requests.get(COIN_URL, headers=self.headers)
        self.status_code = self.url_page.status_code

    def getPage(self):
        return self.url_page.content
    
    def getSoup(self):
        return BeautifulSoup(self.getPage(), features="lxml")
    
    def getTableRow(self):
        table = []
        rows = ''
        soup = self.getSoup()
        table_row = soup.find_all('tr')
        for table_data in table_row:
            for td in table_data.find_all('td'):
                rows += td.text+';'
            table.append(rows)
            #     datas.append
            #     f.writelines(td.text+";")
            # f.write("\n")


        #         data.append(td.text)
        #     datas.append(data)
            
        return table
    # def getTableRow(self):
    #     datas = []
    #     data = []
    #     soup = self.getSoup()
    #     table_row = soup.find_all('tr')
    #     with io.open("fname.txt", "w", encoding="utf-8") as f:
    #         for table_data in table_row:
    #             for td in table_data.find_all('td'):
    #                 f.writelines(td.text+";")
    #             f.write("\n")


    #     #         data.append(td.text)
    #     #     datas.append(data)
            
    #     return "datas"

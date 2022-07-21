from bs4 import BeautifulSoup
import requests
from cryptoDB.db_helper import DatabaseHelper


COIN_URL = 'https://www.livecoinwatch.com'


class CryptoScrapper(object):
    def __init__(self) -> None:
        # create a bot header (user) so as to prevent errors
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        # get the url page
        self.url_page = requests.get(COIN_URL, headers=self.headers)
        # check if it was successful
        self.status_code = self.url_page.status_code

    def getPage(self):
        # get the page data
        return self.url_page.content
    
    def getSoup(self):
        # convert the it to BeautifulSoup so that we can scrape it
        return BeautifulSoup(self.getPage(), features="lxml")
    
    def getTableRow(self):
        # scrape and get all the table rows
        table = []
        soup = self.getSoup()
        table_row = soup.find_all('tr')
        # loop through all the rows
        for table_data in table_row:
            data = ''
            rows = []
            # loop through all the table data and clean them
            for td in table_data.find_all('td'):
                data += td.text+';'
            # add data to rows
            rows.append(data)
            # add rows to table
            table.append(rows)
        # add the whole table to the database
        return DatabaseHelper().addToDatabase(table)
        
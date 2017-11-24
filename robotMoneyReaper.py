import urllib.request as www
import json



class RobotMoneyReaper:
    """
        This robot repear is looking for stocks, in order to identify potecial stocks that could be worth
        in a close future.
    """


    #url = "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=<Symbol>&apikey=<ApiKey>"
    #url =  "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=<Symbol>&interval=1min&apikey=<ApiKey>"

    def __init__(self,stock):
        self.__stock = None
        self.__apiKey = open('apikey.key','r').read()
        self.__url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=<Symbol>&apikey=<ApiKey>"
        self.setStock(stock)

    def setStock(self, stock):
        self.__stock = stock

    def getStock(self):
        return self.__stock

    def __getRetrieveMapStockJson(self):
        #self.__stock = self.getStock()
        self.__url = self.__url.replace('<Symbol>',self.__stock)
        self.__url = self.__url.replace('<ApiKey>',self.__apiKey)
        response = www.urlopen(self.__url)
        data = json.loads(response.read())
        return data

    def getStockRealtime(self):

        try:
            json = self.__getRetrieveMapStockJson()
            for intraday in json['Time Series (Daily)']:

                value = float(json['Time Series (Daily)'][intraday]['4. close'])
                if isinstance(value, float):
                    if value != 0:
                        return value

                break
        except Exception as e:
            print(' ' * 4, "ϟϟϟϟ", e, 'the Interface alphavantage.co failed ₪₪',self.__stock,'₪₪')

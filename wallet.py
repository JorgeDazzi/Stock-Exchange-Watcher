class Wallet:

    def __init__(self, name, money):
        # how much you want to operating in action house
        self.__money = 0.0
        # quantity papers / titles you buy from action house
        self.__papers = 0.0
        # the name of wallet is equal the name of stock
        self.__name = None
        # Stock dots history
        self.__stockVector = None

        # micelanius
        self.dots = 60

        self.setMoney(money)
        self.setName(name)

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setMoney(self, value):
        self.__money = value *1.0

    def getMoney(self):
        return self.__money

    def setPapers(self, value):
        self.__papers = value

    def getPapers(self):
        return self.__papers

    def setStockVector(self, vector):
        self.__stockVector = vector

    def getPortfolioOverview(self):
        overview = [self.getName(), self.getMoney(), self.getPapers(), self.__stockVector.getLastPrice()]
        return overview

    def buyStock(self, amount):
        try:
            text = ''
            if self.getMoney() > 0.0:
                aux = self.getMoney()
                self.setPapers(self.getMoney() / (amount*1.0))
                self.setMoney(0.0)

                text = '    ß R$ %.2f ►► Ƿ %.2f' % (aux, self.getPapers())
                return text
        except Exception as e:
            print(' ' * 4, "ϟϟϟϟ", e , '\n[wallet buyStock = ', self.getName(),']')
            return '.....:.'
        finally:
            return text

    def sellStock(self, amount):
        try:
            text = ''
            if self.getPapers() > 0.0:
                aux = self.getPapers()
                self.setMoney(self.getPapers() * (amount*1.0))
                self.setPapers(0.0)

                text = '    Ṩ Ƿ %.2f ►► R$ %.2f' % (aux , self.getMoney())
                return text
        except Exception as e:
            print(' ' * 4, "ϟϟϟϟ", e, '\n[wallet sellStock = ', self.getName(), ']')
            return '.....:.'
        finally:
            return text


    def getCurrentPortifolio(self):
        print('')
        print('#' * 10, 'Posição atual da Carteira')
        print('#' * 10, 'R$', self.__money)
        print('#' * 10, self.__papers, 'Títulos da ', self.getName())
        print('')
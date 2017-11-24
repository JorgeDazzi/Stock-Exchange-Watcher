from robotMoneyReaper import RobotMoneyReaper
from dots import Dots
import threading
import time


class EvilMinion(threading.Thread):
    """
        Evil Minion is a thread that will seek and destroy the action house
    """

    def __init__(self, wallet, counter):
        threading.Thread.__init__(self)

        self.__flag = 1  # flags >> 1=compra&venda / 2=venda somente / 0=faça porra nenhuma
        self.__minionID = None
        self.__wallet = None
        self.__reaper = None
        self.__amount = 0.0

        self.__wallet = wallet
        self.__reaper = RobotMoneyReaper(self.__wallet.getName())
        self.__dots = Dots(self.__wallet.getName())
        self.__wallet.setStockVector(self.__dots)

        self.setMinionID(self.__wallet.getName())
        self.threadID = self.__wallet.getName() + '_Minion'
        self.name = self.__wallet.getName() + '_Minion'
        self.counter = counter

    def setMinionID(self, id):
        self.__minionID = 'Bananaa-' + id

    def getMinionID(self):
        return self.__minionID

    def getStockRealtime(self):
        print(self.__reaper.getStock(), 'current price =', self.__reaper.getStockRealtime())

    def setFlag(self, num):
        if num in [0,1,2]:
            self.__flag = num
            return True
        else:
            return False

    def getFlag(self):
        return self.__flag

    def getItSellByForce(self):
        try:
            self.setFlag(2)
            self.__amount = self.__reaper.getStockRealtime()
            if self.__amount is not None:
                if self.__amount > 0:
                    text = self.__wallet.getName() + ' ' + self.__wallet.sellStock(self.__amount)
                    self.__dots.setNewDot(self.__amount)
                    return text
        except Exception as e:
            print(' ' * 4, "ϟϟϟϟ", e, '\n', self.__wallet.getName(), 'during the selling force, something got wrong [EvilMinion.run]!')
            return '....:.'

    def run(self):

        time.sleep(2)
        while True:

            #try:
            self.__amount = self.__reaper.getStockRealtime()

            if self.__amount is not None:
                if self.__amount > 0:
                    localtime = time.asctime(time.localtime(time.time()))
                    text = ' ' * 10 + ' '+ localtime + ' '+'♦' * 6+' ' + self.__wallet.getName()+ ' ᴕ previous R$ %.2f Vs current R$ %.2f' % (self.__dots.getLastPrice() , self.__amount)

                    if self.__amount < self.__dots.getLastPrice() and self.__wallet.getMoney() > 0.0:
                        if self.getFlag() == 1:
                            text += self.__wallet.buyStock(self.__amount)
                            self.__dots.setNewDot(self.__amount)
                    elif self.__amount > self.__dots.getLastPrice() and self.__wallet.getPapers() > 0.0:
                        if self.getFlag() in [1,2]:
                            text += self.__wallet.sellStock(self.__amount)
                            self.__dots.setNewDot(self.__amount)

                    print(text)
            #except Exception as e:
                #print(' ' * 4, "ϟϟϟϟ", e, '\n', self.__wallet.getName(), 'something is wrong here [EvilMinion.run]!')

            time.sleep(60)

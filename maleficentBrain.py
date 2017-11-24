from account import Account
import threading
import time

from evilMinion import EvilMinion


class MaleficentBrain(threading.Thread):

    def __init__(self, stockList, budget):
        threading.Thread.__init__(self)

        self.__account = None
        self.__evilMinions = []

        self.threadID = 'MaleficentBrain'
        self.name = 'MaleficentBrain'
        self.counter = 0

        self.setAccount(budget, stockList)

    def setAccount(self, budget, stockList):
        self.__account = Account(budget, stockList)

    def run(self):
        counter = 1
        try:
            for wallet in self.__account.getWallets():
                self.__evilMinions.append(EvilMinion(wallet, counter))
                counter = counter +1
            for minion in self.__evilMinions:
                minion.start()
        except Exception as e:
            print(' ' * 4, "ϟϟϟϟ", e )

        while True:

            try:
                command = input('What do you wish my Lord?\n')

                #Comando de portfolio -f full, consolida os resultados das carteiras
                if command == 'portfolio -f':
                    self.__account.getPortilioConsolidated()

                #consulta o valor de uma ação em tempo real
                elif command == 'stockInfo':

                    id = input('gimme the ID that you are looking for\n')
                    id = 'Bananaa-'+id

                    for minion in self.__evilMinions:

                        if id == minion.getMinionID():
                            minion.getStockRealtime()
                            break

                elif command == 'selling -all':
                    for minion in self.__evilMinions:
                        result = minion.getItSellByForce()
                        print(result)

                elif command == 'stop -all':
                    for minion in self.__evilMinions:
                        minion.setFlag(0)

                elif command == 'resume -all':
                    for minion in self.__evilMinions:
                        minion.setFlag(1)
                    print(' '*6,'All Minions are ready to rock!')

            except Exception as e:
                print(' ' * 4, "ϟϟϟϟ", e, '[Console]')

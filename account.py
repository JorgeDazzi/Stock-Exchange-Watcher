from wallet import Wallet


class Account:

    def __init__(self, budget, stockList):
        # Wallets
        self.__wallets = []
        # The amount in R$ that should the GeniusBrain works
        self.__budget = 0.0

        self.setBudget(budget)
        self.__setTheWallets(stockList)

    def getFullPortfolio(self):
        '''
            print the full portfolio
        '''
        if self.__wallets is not None:
            if len(self.__wallets) > 0:
                for wallet in self.__wallets:
                    print('')
                    print('$'*60)
                    print('')
                    print('#'*10, 'Carteira ', wallet.getName())
                    print('#'*10, 'R$', wallet.getMoney())
                    print('#'*10, 'Papeis ', wallet.getPapers())
                    print('')
                    print('$' * 60)
                    print('')

    def setBudget(self, value):
        '''
        definy the amount in R$
        :param value: float that represent R$ amount
        '''
        self.__budget = value

    def getBudget(self):
        '''
        request the valor in Budget
        :return: budget in float
        '''
        return self.__budget

    def getWallets(self):
        return self.__wallets

    def __setTheWallets(self, stockList):
        #initializer the wallets

        if stockList is not None:
            if len(stockList) > 0:
                for stock in stockList:
                    self.__wallets.append(Wallet(stock, self.getBudget()))

    def getPortilioConsolidated(self):
        if self.getWallets() is not None:
            total = 0.0
            print('¨' * 60)
            for wallet in self.getWallets():
                walletInfo = wallet.getPortfolioOverview()
                print('֍'*10, ' ',walletInfo[0], ' '*4, 'R$ ','%.2f'%walletInfo[1], ' '*4, ' Ƿ', '%.2f'%walletInfo[2], ' '*4, 'Previous R$','%.2f'%walletInfo[3])
                total += walletInfo[1]
            print('֍' * 10, 'Total = %.2f'%total)
            print('¨' * 60)
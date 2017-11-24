import time as t


class Dots:

    def __init__(self, dotId):
        self.__dotID = None
        self.__coordinates = []
        self.__coordinates.append([9999999, t.time() - 20.0])
        self.setDotID('Dot.'+dotId)

    def getDotID(self):
        return self.__dotID

    def setDotID(self, dotId):
        self.__dotID = dotId

    def setNewDot(self, dot):
        try:
            self.__coordinates.insert(0, [dot, t.time()])
        except Exception as e:
            print(' ' * 4, 'ϟϟϟϟ', e, 'Error during insert a new dot')
        finally:
            if len(self.__coordinates) > 10:
                self.__coordinates = self.__coordinates[:6] #clean the array, it'll avoid out of memory and lets the app running faster

    def getDots(self):
        return self.__coordinates[:3]

    def getLastPrice(self):
        if len(self.__coordinates) > 0:
            return self.__coordinates[0][0]
        return None
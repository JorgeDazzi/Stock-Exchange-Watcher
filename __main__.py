from maleficentBrain import MaleficentBrain
import sys

"""
@Pizza
"""

stockList = ['GOLL4.SA', 'AZUL4.SA', 'CCRO3.SA','BBAS3.SA', 'BBDC4.SA', 'WEGE3.SA', 'EMBR3.SA', 'BRFS3.SA' , 'BBSE3.SA','ECOR3.SA', 'MPLU3.SA','MOVI3.SA']
#stockList = ['GOLL4.SA']

if __name__ == '__main__':
    mindHunter = MaleficentBrain(stockList, 1000.00)
    mindHunter.start()